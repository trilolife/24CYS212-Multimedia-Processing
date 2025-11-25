from PIL import Image

def median_cut_quantize(input_path,output_path,num_colours=16):
    img=Image.open(input_path).convert("RGB")
    quantized_img=img.quantize(num_colours,method=0)
    quantized_img=quantized_img.convert("RGB")
    quantized_img.save(output_path)

num_colours=int(input("Enter the number of colours: "))
median_cut_quantize("image.jpg","output.jpg",num_colours)
