from PIL import Image

def octree_quantization(input_path,output_path,num_colours):
    img=Image.open(input_path).convert("RGB")
    print(f"Quantizing image to a maximum of {num_colours} colours using FASTOCTREE Method.")
    quantized_img=img.quantize(colors=num_colours,method=Image.Quantize.FASTOCTREE)
    quantized_img=quantized_img.convert("RGB")
    quantized_img.save(output_path)
    print(f"Image saved to {output_path}")

num_colours=int(input("Enter the number of colours to quantize: "))
octree_quantization("image.jpg","oct_out.jpg",num_colours)
