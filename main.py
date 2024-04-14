class_template = '''
class {class_name}:
    def __init__(self, {constructor_args}):
        {init_body}
'''

def generate_class_file(class_name, constructor_args, init_body, file_path):
    class_content = class_template.format(
        class_name=class_name,
        constructor_args=constructor_args,
        init_body=init_body
    )

    with open(file_path, 'w') as file:
        file.write(class_content)

# Example usage:
class_name = "ExampleClass"
constructor_args = "database, env"
init_body = "self.database = database\n        self.env = env"

generate_class_file(class_name, constructor_args, init_body, "example_class.py")