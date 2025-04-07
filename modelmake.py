import argparse
import trimesh
import os

def convert(input_file, output_file, format):
    try:
        mesh = trimesh.load(input_file)
        
        valid_formats = ['obj', 'stl', 'fbx', 'ply']
        if format not in valid_formats:
            print(f"Error: Unsupported format '{format}'. Supported formats are: {', '.join(valid_formats)}")
            return
        
        mesh.export(output_file, file_type=format)
        print(f"Model converted successfully to {format} format: {output_file}")
    except Exception as e:
        print(f"Error converting model: {e}")

def scale(input_file, scale_factor):
    try:
        mesh = trimesh.load(input_file)
        
        mesh.apply_scale(scale_factor)
        
        file_name, file_extension = os.path.splitext(input_file)
        output_file = f"{file_name}_scaled{file_extension}"
        
        mesh.export(output_file)
        print(f"Model scaled by {scale_factor} and saved to: {output_file}")
    except Exception as e:
        print(f"Error scaling model: {e}")

def optimize(input_file, output_file):
    try:
        mesh = trimesh.load(input_file)

        print(f"Loaded object type: {type(mesh)}")

        if isinstance(mesh, trimesh.Scene):
            print("Loaded object is a Scene. Dumping meshes into a single object.")
            
            meshes = mesh.dump()
            print(f"Meshes in the scene: {len(meshes)}")
            
            if len(meshes) > 0:
                for idx, mesh in enumerate(meshes):
                    optimized_mesh = mesh.subdivide()
                    
                    file_name, file_extension = os.path.splitext(output_file)
                    output_mesh_file = f"{file_name}_optimized_{idx}{file_extension}"
                    
                    optimized_mesh.export(output_mesh_file)
                    print(f"Optimized mesh {idx} saved to: {output_mesh_file}")
            else:
                print("Error: The scene contains no meshes.")
                return
        else:
            print("Error: Loaded object is not a valid scene.")
        
    except Exception as e:
        print(f"Error optimizing model: {e}")

def main():
    parser = argparse.ArgumentParser(description="ModelMake3D: A command-line tool for 3D model format conversion, scaling, and optimization.")
    
    parser.add_argument("action", choices=["convert", "scale", "optimize"], help="Action to perform (convert, scale, optimize).")
    parser.add_argument("input", help="Input file path for the model.")
    parser.add_argument("output", help="Output file path for saving the processed model.")
    
    parser.add_argument("--scale", type=float, help="Scale factor (e.g., 0.5 for shrinking, 2.0 for enlarging).")
    parser.add_argument("--format", type=str, help="Format to convert to (e.g., 'obj', 'fbx', 'stl').")
    
    args = parser.parse_args()

    if args.action == "convert":
        if not args.format:
            print("Error: Please specify the output format using --format (e.g., 'obj', 'fbx', 'stl').")
            return
        convert(args.input, args.output, args.format)
    
    elif args.action == "scale":
        if args.scale is None:
            print("Error: Please provide a scale factor using --scale (e.g., 0.5 for shrinking, 2.0 for enlarging).")
            return
        scale(args.input, args.scale)
    
    elif args.action == "optimize":
        optimize(args.input, args.output)

if __name__ == "__main__":
    main()

