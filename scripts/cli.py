""" This file provides an entry point to CLI scripts. """

import click

import transformers


@click.command()
@click.argument('transform_names', nargs=-1)
@click.option(
    '--source', 
    default='../templates/cyoa.html', 
    help="File to read data from.")
@click.option(
    '--target', 
    default='../templates/cyoa_new.html', 
    help="File to write data to.")
def apply_transforms(transform_names, source, target):
    """
    Transformers to implement (processed from left to right).
    
    - recommend_to_id: Transforms "You should watch {title}" to "Open #{id(title)}"
    
    - id_to_drawer: Transforms "Open #{id}" to "Open drawer #{id}"
    """
    
    # Load transformer objects
    transforms = (
        transformers.get_generator_function(name)
        for name in transform_names)
    
    with open(source, 'r') as source_file, open(target, 'w') as target_file:
        # Process all transforms on the source data
        data = iter(source_file)
        for transform in transforms:
            data = transform(data)
        
        # Write the fully transformed data to the target file
        for line in data:
            target_file.write(line)

if __name__ == '__main__':
    apply_transforms()