###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

# imports the libaries used within totems+
from email.utils import format_datetime
from PIL import Image
import os, shutil, getpass

# defines the texture convereter subroutine
def ANIM(imageLocation, packName, integrationType, rename):

    # opens the image as an object python/PIL can interact with
    imageObject = Image.open(imageLocation)
    
    # calculates the height for the new image
    height = imageObject.size[1] * imageObject.n_frames

    # creates the new image using the calacuated height
    new = Image.new(mode="RGB", size=(imageObject.size[1], height), color='#ffffff')

    # calacuates the buffer zone required for the image to be centeral
    buffer = imageObject.size[0] - imageObject.size[1]
    buffer = round(buffer/2)

    # for each frame in the gif
    for frame in range(0,imageObject.n_frames):

        # selects said frame
        imageObject.seek(frame)

        # calacutes the height at which the image needs to be pasted 
        # depends on how far down the new image you are
        height2 = frame * imageObject.size[1]

        # pastes the image using the calculated buffer and height
        new.paste(imageObject, (-buffer, height2))

     # if the directory resized already exists, then delete it
    if os.path.exists('C:/Users/' + getpass.getuser() + '/AppData/Roaming/Totems+/giftexture'):
        shutil.rmtree('C:/Users/' + getpass.getuser() + '/AppData/Roaming/Totems+/giftexture')

    # make the resized folder
    os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/giftexture")

    locationList = imageLocation.split("/")

    # saves the new image
    new.save("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/giftexture/" + locationList[-1])

    # sets frametime to a temporary constant (it will be variable in the future)
    FRAMETIME = 1

    if integrationType == "MCCMD":

        file = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + packName + "/assets/minecraft/textures/totems/" + locationList[-1] + ".mcmeta", "w+")

        file.writelines(['{\n',
        '  "animation": {\n'])
        file.write('    "frametime": ' + FRAMETIME + '\n')
        file.writelines(['  }\n',
        '}'])

        file.close()

    elif integrationType == "OFCIT":

        file = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + packName + "/assets/minecraft/optifine/cit/totems/" + str(rename.lower()) + "/" + locationList[-1] + ".mcmeta", "w+")

        file.writelines(['{\n',
        '  "animation": {\n'])
        file.write('    "frametime": ' + FRAMETIME + '\n')
        file.writelines(['  }\n',
        '}'])

        file.close()

    return "C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/giftexture" + locationList[-1]

# runs the subroutine for testing purposes
ANIM("img/test.gif")