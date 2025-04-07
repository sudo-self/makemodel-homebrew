import sys
import argparse

def list_commands():
    print("""
    ModelMake3D Command-Line Tool - Available Commands

    1. Convert
       Description: Convert a 3D model to another format.
       Usage: python modelmake3d.py convert <input_file> <output_file> --format <format>
       Example: python modelmake3d.py convert model.obj model.fbx --format fbx

    2. Scale
       Description: Scale a 3D model by a specific factor.
       Usage: python modelmake3d.py scale <input_file> <output_file> --scale <scale_factor>
       Example: python modelmake3d.py scale model.obj model_scaled.obj --scale 0.5

    3. Optimize
       Description: Optimize a 3D model by reducing polygons.
       Usage: python modelmake3d.py optimize <input_file> <output_file>
       Example: python modelmake3d.py optimize model.obj model_optimized.obj

    General Options:
    -h, --help       Show this help message and exit
    --format         The format to convert the model to (e.g., 'obj', 'fbx', 'stl')
    --scale          The scale factor (e.g., 0.5 for 50% scaling)

    """)
  
def main():
    if len(sys.argv) == 1 or sys.argv[1] == "help":
        list_commands()
    else:
        print("Invalid command or arguments. Use 'python modelmake3d.py' to view the available commands.")

if __name__ == "__main__":
    main()


