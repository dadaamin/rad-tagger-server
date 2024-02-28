# Here's a simple Python script for a server using the Flask micro web framework.
# The server receives text through a POST request and repeats it back to the client.

import spacy
from scispacy.linking import EntityLinker
import json

from umls_to_label_mapping import label_mapping


from flask import Flask, request


app = Flask(__name__)

nlp = spacy.load("en_core_sci_sm")
nlp.add_pipe("scispacy_linker", config={"resolve_abbreviations": False, "linker_name": "umls", "threshold": 0.5})

linker = nlp.get_pipe("scispacy_linker")

seg_entities = []

with open("umls_mapping.json") as f:
    for json_entity in f:
        seg_entities.append(json.loads(json_entity))

with open("class_list.json") as f:
    seg_class_list = json.load(f)["categories"]

def link_to_seg_ent(text):

    for ent in seg_entities:
        for concept in ent["umls_concepts"]:
            if concept.lower() in text.lower():
                return ent["class"]
    return None

def find_label_id(label):
    for c in seg_class_list:
        if c["name"] == label:
            return c["id"]
    return -1

@app.route('/tag', methods=['POST'])
def tag_text():
    data = request.get_json()
    text = data['text']
    doc = nlp(text)

    tags = []
    offset = 0
    for ent in doc.ents:
            # Each entity is linked to UMLS with a score
            # (currently just char-3gram matching).
            if ent._.kb_ents:
                seg_ent = link_to_seg_ent(linker.kb.cui_to_entity[ent._.kb_ents[0][0]].canonical_name)
                if seg_ent:
                    # map to segmentation labels
                    seg_labels = []
                    if "mappings" in label_mapping[seg_ent]:
                        for keys, value in label_mapping[seg_ent]["mappings"]:
                            if all(k.lower() in str(ent).lower() for k in keys):
                                if isinstance(value, str):
                                    value = [value]
                                seg_labels = value
                    if not seg_labels:
                        seg_labels = [label_mapping[seg_ent]["default"]]
                    seg_labels = [str(find_label_id(l)) for l in seg_labels]
                    seg_labels = ",".join(seg_labels)
                    text = f"{text[:ent.start_char + offset]}{str(ent)}[{seg_labels}]"
                    offset += len(seg_labels) + 2
    
    return {'tags': text}

# To run the server, use the following command in the terminal:
# flask run
# This will start the server on http://127.0.0.1:5000/

# To send a request to this server, you can use a tool like curl or Postman.
# Here's an example of a curl command to send a POST request with text:
# curl -X POST http://127.0.0.1:5000/repeat -H "Content-Type: application/json" -d '{"text":"Hello, World!"}'

if __name__ == '__main__':
    

    app.run(host='0.0.0.0', use_reloader=False)
