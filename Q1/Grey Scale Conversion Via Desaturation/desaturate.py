from PIL import Image

def desaturate_image(input_path,output_path):
    img=Image.open(input_path).convert("RGB")
    width,height=img.size
    gray_img=Image.new("RGB",(width,height))
    for x in range(width):
        for y in range(height):
            r,g,b=img.getpixel((x,y))
            max_val=max(r,g,b)
            min_val=min(r,g,b)
            gray=int((max_val+min_val)/2)
            gray_img.putpixel((x,y),(gray,gray,gray))
    gray_img.save(output_path)
    print("Saved: ",output_path)

desaturate_image("image.jpg","desat_out.jpg")
