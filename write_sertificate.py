from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
def write_attestat_image(degree,author,student,channel):  
    # 1. Open the image
    # Make sure "input_image.jpg" is in the same directory or provide the full path
    image = Image.open("images/attestat.jpg")
    import textwrap
    # 2. Create a drawing context
    draw = ImageDraw.Draw(image)
    # 3. Define the text and position
    name = f"{student}"
    if  float(degree) >86:  
        degree_=f"Telegramdagi «{channel}» kanali orqali @Aqilli_testbot asosida tashkil etilgan attestatsiya test sinovlarida {degree} % natija ko‘rsatib, belgilangan talablar asosida 'Oliy malaka toifasi va 70 foizlik ustama'ni qo‘lga kiritganligi munosabati bilan ushbu sertifikat topshirildi."
    elif 80<float(degree)<=86:
        degree_=f"Telegramdagi «{channel}» kanali orqali @Aqilli_testbot asosida tashkil etilgan attestatsiya test sinovlarida {degree} natija ko‘rsatib, belgilangan talablar asosida 'oliy malaka toifasi'ni qo‘lga kiritganligi munosabati bilan ushbu sertifikat topshirildi."
    elif 70<float(degree)<=80:
        degree_=f"Telegramdagi «{channel}» kanali orqali @Aqilli_testbot asosida tashkil etilgan attestatsiya test sinovlarida {degree} natija ko‘rsatib, belgilangan talablar asosida '1 malaka toifasi'ni qo‘lga kiritganligi munosabati bilan ushbu sertifikat topshirildi."
    elif 60<float(degree)<=70:
        degree_ = f"Telegramdagi «{channel}» kanali orqali @Aqilli_testbot asosida tashkil etilgan attestatsiya test sinovlarida {degree} natija ko‘rsatib, belgilangan talablar asosida '1 malaka toifasi'ni qo‘lga kiritganligi munosabati bilan ushbu sertifikat topshirildi."
    elif 55<float(degree)<=60:
        degree_ = f"Telegramdagi «{channel}» kanali orqali @Aqilli_testbot asosida tashkil etilgan attestatsiya test sinovlarida {degree} natija ko‘rsatib, belgilangan talablar asosida 'Mutahasis malaka toifasi'ni qo‘lga kiritganligi munosabati bilan ushbu sertifikat topshirildi."
    else:
        degree_=f"Telegramdagi «{channel}» kanali orqali @Aqilli_testbot asosida tashkil etilgan attestatsiya test sinovlarida ishtirok etib, test natijalariga asosan {degree} ball to'plaganligi munosabati bilan ushbu sertifikat bilan taqdirlandi."
        
    # Coordinates (x, y) for the top-left corner of the text
    position_name = (400, 310)
    position_date = (330, 670) 
    position_degree_ = (250, 420) 
    position_author = (780, 670) 
    # Color in RGB format (e.g., black is (0, 0, 0), white is (255, 255, 255))
    text_color = (255, 255, 255) 
    from datetime import date
    today = str(date.today())
    author = f'{author}'
    # 4. Load a font (optional, uses a default if not specified)
    # You need a TrueType Font (.ttf) file (e.g., "arial.ttf"). 
    # You can download fonts from Google Fonts.
    try:
        font_name = ImageFont.truetype("/bot/arial.ttf", 65) # Specify font file and size
        font_date = ImageFont.truetype("/bot/arial.ttf", 30)
        font_author = ImageFont.truetype("/bot/arial.ttf", 35)
        font_degree_ = ImageFont.truetype("/bot/arial.ttf", 25)
    except IOError:
        font_name = ImageFont.load_default() 
        font_author = ImageFont.load_default() 
        font_date = ImageFont.load_default()
        font_degree_ = ImageFont.load_default()  
        # Fallback to default font if file not found
        print("Custom font not found, using default.")

    # 5. Add the text to the image
    draw.text(position_name, name.title(), fill=text_color, font=font_name)
    draw.text(position_author, author.title(), fill=text_color, font=font_author)
    draw.text(position_date, today, fill=text_color, font=font_date)
    wrapped_text = textwrap.fill(degree_, width=75)
    draw.multiline_text(position_degree_, wrapped_text, font=font_degree_, fill=text_color, spacing=10)
        
    # 6. Save the resulting image
    bio = BytesIO()
    bio.name = "image.png"   # IMPORTANT for Telegram
    image.save(bio, format="PNG")
    bio.seek(0)
    return bio
    # return image.show()
def write_simple_image(degree,author,student):  
    # 1. Open the image
    # Make sure "input_image.jpg" is in the same directory or provide the full path
    image = Image.open("images/school.jpg")
    import textwrap
    # 2. Create a drawing context
    draw = ImageDraw.Draw(image)
    # 3. Define the text and position
    name = f"{student}"
    degree_=f"@Aqilli_testbot yordamida tashkil etilgan  test sinovlarida ishtirok etib, test natijalariga ko‘ra {degree} ball to‘plaganligi munosabati bilan ushbu sertifikat bilan taqdirlandi."
    # Coordinates (x, y) for the top-left corner of the text
    position_name = (400, 330)
    position_date = (330, 670) 
    position_degree_ = (250, 420) 
    position_author = (780, 670) 
    # Color in RGB format (e.g., black is (0, 0, 0), white is (255, 255, 255))
    text_color = (255, 255, 255) 
    from datetime import date
    today = str(date.today())
    author = f'{author}'
    # 4. Load a font (optional, uses a default if not specified)
    # You need a TrueType Font (.ttf) file (e.g., "arial.ttf"). 
    # You can download fonts from Google Fonts.
    try:
        font_name = ImageFont.truetype("/bot/arial.ttf", 65) # Specify font file and size
        font_date = ImageFont.truetype("/bot/arial.ttf", 30)
        font_author = ImageFont.truetype("/bot/arial.ttf", 35)
        font_degree_ = ImageFont.truetype("/bot/arial.ttf", 30)
    except IOError:
        font_name = ImageFont.load_default() 
        font_author = ImageFont.load_default() 
        font_date = ImageFont.load_default()
        font_degree_ = ImageFont.load_default()  

    # 5. Add the text to the image
    draw.text(position_name, name.title(), fill=text_color, font=font_name)
    draw.text(position_author, author.title(), fill=text_color, font=font_author)
    draw.text(position_date, today, fill=text_color, font=font_date)
    wrapped_text = textwrap.fill(degree_, width=60)
    draw.multiline_text(position_degree_, wrapped_text, font=font_degree_, fill=text_color, spacing=10)
   
    # 6. Save the resulting image
    bio = BytesIO()
    bio.name = "image1.png"   # IMPORTANT for Telegram
    image.save(bio, format="PNG")
    bio.seek(0)
    return bio
    # return image.show()
def write_school_image(degree,author,student,class_number,subject):  
    # 1. Open the image
    # Make sure "input_image.jpg" is in the same directory or provide the full path
    image = Image.open("images/school.jpg")
    import textwrap
    # 2. Create a drawing context
    draw = ImageDraw.Draw(image)
    # 3. Define the text and position
    name = f"{student}"
    degree_=f"@Aqilli_testbot yordamida tashkil etilgan {class_number}-sinf o‘quvchilari uchun {subject} fanidan o‘tkazilgan test sinovlarida ishtirok etib, test natijalariga ko‘ra {degree} ball to‘plaganligi munosabati bilan ushbu sertifikat bilan taqdirlandi."
    # Coordinates (x, y) for the top-left corner of the text
    position_name = (400, 330)
    position_date = (330, 670) 
    position_degree_ = (250, 420) 
    position_author = (780, 670) 
    # Color in RGB format (e.g., black is (0, 0, 0), white is (255, 255, 255))
    text_color = (255, 255, 255) 
    from datetime import date
    today = str(date.today())
    author = f'{author}'
    # 4. Load a font (optional, uses a default if not specified)
    # You need a TrueType Font (.ttf) file (e.g., "arial.ttf"). 
    # You can download fonts from Google Fonts.
    try:
        font_name = ImageFont.truetype("/bot/arial.ttf", 65) # Specify font file and size
        font_date = ImageFont.truetype("/bot/arial.ttf", 30)
        font_author = ImageFont.truetype("/bot/arial.ttf", 35)
        font_degree_ = ImageFont.truetype("/bot/arial.ttf", 25)
    except IOError:
        font_name = ImageFont.load_default() 
        font_author = ImageFont.load_default() 
        font_date = ImageFont.load_default()
        font_degree_ = ImageFont.load_default()  

    # 5. Add the text to the image
    draw.text(position_name, name.title(), fill=text_color, font=font_name)
    draw.text(position_author, author.title(), fill=text_color, font=font_author)
    draw.text(position_date, today, fill=text_color, font=font_date)
    wrapped_text = textwrap.fill(degree_, width=75)
    draw.multiline_text(position_degree_, wrapped_text, font=font_degree_, fill=text_color, spacing=10)
        
    # 6. Save the resulting image
    bio = BytesIO()
    bio.name = "image1.png"   # IMPORTANT for Telegram
    image.save(bio, format="PNG")
    bio.seek(0)
    return bio
    # return image.show()
# write_attestat_image(degree='55',author='Behzod',student='Asliddinov Behzod',channel='Behzod')