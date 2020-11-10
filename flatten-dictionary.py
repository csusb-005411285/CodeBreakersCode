class Solution:
    def __init__(self):
        self.flattened_obj = {}
    
    def flatten_dict(self, obj):
        self.flatten_dict_helper(obj, '')
        return self.flattened_obj
    
    def flatten_dict_helper(self, obj, parent_key):
        for k, v in obj.items():
            if isinstance(v, dict):
                if k == '' and parent_key == '':
                    self.flatten_dict_helper(obj[k], parent_key, flattened_obj)
                elif k != '':
                    if parent_key != '':
                        self.flatten_dict_helper(obj[k], parent_key + '.' + k)
                    else:
                        self.flatten_dict_helper(obj[k], k)
                elif parent_key != '':
                    self.flatten_dict_helper(obj[k], parent_key)
            else:
                if k != '':
                    if parent_key:
                        self.flattened_obj[parent_key + '.' + k] = v
                    else:
                        self.flattened_obj[k] = v
                elif parent_key != '':
                    self.flattened_obj[parent_key] = v
        return
