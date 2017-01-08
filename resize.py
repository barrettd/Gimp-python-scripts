# --------------------------------------------------------------------------------------------
# Image collection generation.
# I used this python script to generate a number of scaled images for Apple device slices.
#
# Run from Gimp->Filters->Python-Fu console
#
# Assume that we have a collection of related images that are scaled the same way
# to the Apple device slices.
#
# We choose one image as the 'key image' that the other images use for resizing ratios.
# 8 Jan 2017 - Barrett Davis
# --------------------------------------------------------------------------------------------

def load_png( directory, filebase ):
    filetype = '.png'
    filename = filebase + filetype
    filepath = directory + filename
    return pdb.file_png_load(filepath, filename)

def export_png( img, width, height, directory, filebase, descriptor ):
    filetype = '.png'
    filename = filebase + '_' + descriptor + filetype
    filepath = directory + filename
    dupe = pdb.gimp_image_duplicate(img)
    dupe.scale( width, height )
    layer = pdb.gimp_image_merge_visible_layers(dupe, CLIP_TO_IMAGE)
    #    print 'saving ' + filepath
    pdb.file_png_save2(dupe, layer, filepath, filename,1,9,1,1,1,1,1,0,1)
    pdb.gimp_image_delete(dupe)

def generate_png( img, keySize, key1xSize, multiplier, directory, filebase, descriptor ):
    ratio = (float(key1xSize) * float( multiplier )) / float(keySize)
    width  = int(round( float( img.width )  * ratio ))
    height = int(round( float( img.height ) * ratio ))
    export_png( img, width, height, directory, filebase, descriptor )

def generate_iphone( img, keySize, key1xSize, directory, filebase ):
    descriptor = 'iPhone'
    generate_png( img, keySize, key1xSize, 1.0, directory, filebase, descriptor + '1x')
    generate_png( img, keySize, key1xSize, 2.0, directory, filebase, descriptor + '2x')
    generate_png( img, keySize, key1xSize, 3.0, directory, filebase, descriptor + '3x')

def generate_ipad( img, keySize, key1xSize, directory, filebase ):
    descriptor = 'iPad'
    generate_png( img, keySize, key1xSize, 1.0, directory, filebase, descriptor + '1x')
    generate_png( img, keySize, key1xSize, 2.0, directory, filebase, descriptor + '2x')

def generate_apple_tv( img, keySize, key1xSize, directory, filebase ):
    descriptor = 'AppleTV'
    generate_png( img, keySize, key1xSize, 1.0, directory, filebase, descriptor + '1x')

def generate_mac( img, keySize, key1xSize, directory, filebase ):
    descriptor = 'Mac'
    generate_png( img, keySize, key1xSize, 1.0, directory, filebase, descriptor + '1x')
    generate_png( img, keySize, key1xSize, 2.0, directory, filebase, descriptor + '2x')


# Images
imageDir  = '/Volumes/Data/Pictures/Games/tumble/master/'
pngType   = '.png'

# Bot - key image
botName   = 'bot'
botDir    = imageDir + botName + '/'
botImage  = load_png( botDir, botName );

# Collar
collarName   = 'collar'
collarDir    = imageDir + collarName + '/'
collarImage  = load_png( collarDir, collarName );

# Strut
strutName   = 'strut'
strutDir    = imageDir + strutName + '/'
strutImage  = load_png( strutDir, strutName );

# Sizes should be float
keySize = float(botImage.height)   # All resizing keys off of the bot height
iPhone1xSize =  64.0          # Bot height for iPhone 1x
iPad1xSize   = 154.0          # Bot height for iPad 1x
tv1xSize     = 154.0          # Bot height for Apple TV 1x
mac1xSize    = 288.0          # Bot height for Mac 1x

# iPhone scale
generate_iphone(    botImage, keySize, iPhone1xSize,    botDir,    botName )
generate_iphone( collarImage, keySize, iPhone1xSize, collarDir, collarName )
generate_iphone(  strutImage, keySize, iPhone1xSize,  strutDir,  strutName )

# iPad scale
generate_ipad(    botImage, keySize, iPad1xSize,    botDir,    botName )
generate_ipad( collarImage, keySize, iPad1xSize, collarDir, collarName )
generate_ipad(  strutImage, keySize, iPad1xSize,  strutDir,  strutName )

# Apple TV scale
generate_apple_tv(    botImage, keySize, tv1xSize,    botDir,    botName )
generate_apple_tv( collarImage, keySize, tv1xSize, collarDir, collarName )
generate_apple_tv(  strutImage, keySize, tv1xSize,  strutDir,  strutName )

# Mac scale
generate_mac(    botImage, keySize, mac1xSize,    botDir,    botName )
generate_mac( collarImage, keySize, mac1xSize, collarDir, collarName )
generate_mac(  strutImage, keySize, mac1xSize,  strutDir,  strutName )



