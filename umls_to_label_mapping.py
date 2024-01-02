label_mapping = {
    "ETT": {
        # Merge ETT - Normal, NGT - Incompletely Imaged, ETT - Borderline, ETT - Abnormal
        "default": "ETT"
    },
    "object": {
        # How to map clips, drain, wires, ... ?
        "mappings": [
            (["pacemaker"], "electronics")
            ],
        "default": "foreign object"
    },
    "cardiomediastinum": {
        "default": "cardiomediastinum" 
    },
    "lung": {
        "mappings": [
            (["nodule"], "Nodule"),
            (["base"], "lung base"),
            (["consolidation"], "Consolidation"),
            # Merge lung upper lobe left and lung upper lobe right
            (["upper", "lobe"], "lung upper lobe"),
            (["upper", "zone"], "upper zone lung"),
            (["lower", "lobe"], "lung lower lobe"),
            (["lower", "zone"], "lower zone lung"),
            (["right", "base"], "right lung base"),
            (["left", "base"], "left lung base"),
            (["scarring"], "Fibrosis"),
            (["fibrosis"], "Fibrosis"),
            (["atelectasis"], "Atelectasis"),
            (["collapse"], "Atelectasis"),
            (["pneumothorax"], "Pneumothorax"),
            (["base"], "lung base"),
            ],
        "default": "lung"
    },
    "organ": {
        "mappings": [(["esophagus"], "esophagus"),
                     (["stomach"], "stomach"),
                    ]

    },
    "abdomen": {
        "mappings": [(["stomach"], "stomach")]
    },
    "pleural effusion": {
        "default": "Effusion"
    },
    "heart": {
        "mappings": [
            (["right", "ventricle"], "heart ventricle right"),
            (["left", "ventricle"], "heart ventricle left"),
            (["right", "ventricular"], "heart ventricle right"),
            (["left", "ventricular"], "heart ventricle left"),
            (["left", "atrium"], "heart ventricle left"),
            (["right", "atrium"], "heart ventricle right"),
            ],
        "default": "heart"
    },
    "Lung pathology": {
        "mappings": [
            (["opacities"], ["Consolidation", "Diffuse Nodule", "Effusion", "Mass", "Nodule"]),
            (["opacity"], ["Consolidation", "Diffuse Nodule", "Effusion", "Mass", "Nodule"]),
            (["consolidation"], "Consolidation"),

        ],
        "default": "lung"
    },
    "collapsed": {
        "default": "Atelectasis"
    },
    "pulmonary vasculature": {
        "default": "pulmonary artery"
    },
    "areal lesion": {
        "default": "Areal Lesion"
    },
    "aorta": {
        "mappings": [
            (["arch"], "aortic arch"),
            (["descending"], "descending aorta"),
            (["ascending"], "ascending aorta"),
        ],
        "default": "aorta"
    },
    "calcification": {
        "default": "Calcification"
    },
    "fracture": {
        "mappings": [
            (["rib"], ["Fracture", "rib_cartilage"])
        ],
        "default": "Fracture"
    },
    "surgery": {
        # ???
        "default": "[surgery]"
    },
    "spine": {
        "default": "spine"
    },
    "diaphragm": {
        "mappings": [
            (["left", "hemidiaphragm"], "left hemidiaphragm"),
            (["right", "hemidiaphragm"], "right hemidiaphragm"),
        ],
        "default": "diaphram"
    },
    "device": {
        # drain, wires, clips?
        "mappings": [
            (["pacemaker"], "electronics"),
        ],
        "default": "foreign object"

    },
    "NGT": {
        # Merge NGT - Normal, NGT - Incompletely Imaged, NGT - Borderline, NGT - Abnormal
        "default": "NGT"
    },
    "esophagus": {
        "default": "esophagus"
    },
    "organ": {
        "mappings": [
            (["esophagus"], "esophagus"),
            (["duodenum"], "duodenum"),
            (["small bowel"], "small bowel"),
            (["stomach"], "stomach"),
        ],
        # ????
        "default": "[organ]"
    },
    "lung right": {
        "mappings": [
            (["base"], "right lung base"),
            (["suprahilar"], "right upper zone lung"),
            (["upper", "lobe"], "lung upper lobe right"),
            (["lower", "lobe"], "lung lower lobe right"),
            (["mid"], "right mid zone lung"),
        ],
        "default": "right lung"
    },
    "abdomen": {
        # ?
        "default": "stomach"
    },
    "pleural pathology": {
        "mappings": [
            (["pneumothorax"], "Pneumothorax"),
            (["scarring"], "Fibrosis"),
            (["thickening"], "Pleural Thickening"),
            (["effusion"], "Effusion"),

        ],
        # ???
        "default": "[pleural pathology]"
    },
    "CVC": {
         # Merge CVC - Normal, CVC - Incompletely Imaged, CVC - Borderline, CVC - Abnormal
        "default": "CVC"
    },
    "lung left": {
        "mappings": [
            (["base"], "left lung base"),
            (["suprahilar"], "left upper zone lung"),
            (["upper", "lobe"], "lung upper lobe left"),
            (["lower", "lobe"], "lung lower lobe left"),
            (["mid"], "left mid zone lung"),
        ],
        "default": "left lung"
    },
    "non consolidated lesion": {
        # only one annotation
    },
    "trachea": {
        "default": "trachea"
    },
    "thoracic spine": {
        "default": "thoracic spine"
    },
    "clavicles": {
        "mappings": [
            (["left"], "clavicle left"),
            (["right"], "clavicle right"),
        ],
        "default": "clavic"

    },
    "lumbar spine": {
        "default": "lumbar spine"
    },
    "cervical spine": {
        "default": "cervical spine"
    },
    "rib": {
        # TODO: parse numbers from strings to map ribs
        "default": "rib_cartilage"
    },
    "breast": {
        "mappings": [
            (["left"], "breast left"),
            (["right"], "breast right"),
        ],
        "default": "breast"
    },
    "posterior rib right": {
        #merge with rib
        "default": "rib_cartilage"
    },
    "swan ganz catheter": {
        "default": "Swan Ganz Catheter Present"
    },
    "rib_cartilage": {
        "default": "rib_cartilage"
    },
    "sternum": {
        "default": "sternum"
    },

    
    
      
}