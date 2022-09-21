    #  /data/
    #  |    |input/  
    #  |    |       |rain/   
    #  |                    |0000000.png
    #  |                    |0000001.png
    #  |                    |...
    #  |    |       |flare/ 
    #  |                    |0000000.png
    #  |                    |0000001.png
    #  |                    |...
    #  |    |       |affine/
    #  |                    |0000000.png
    #  |                    |0000001.png
    #  |                    |...
    #  |            |.../
    #  |    |depth/  
    #  |            |0000000.png
    #  |            |0000000_affine.png
    #  |            |0000001.png
    #  |            |0000001_affine.png
    #  |            |...
    #  | split_file.txt


def copy_images():

    pass
    # Open split file
    with open('split_file.txt') as f:
        lines = f.readlines()
    # For each line:
    for line in lines:
        
        # If first file exists AND second file exists:

        #   For each augmentation type:
        #   if <augmentation_type> is <affine>:
        #      Perform augmentation on rgb image
        #      Perform augmentation on depth image
        #      Save rgb file with new name in /<input/affine> folder
        #      Save augmented depth file as <depth/xxxxxx_affine.png> 
        #      insert [rgb_file, depth_file, augmentation_type] into list
        #   else:
        #      Perform augmentation   
        #      Save file with new name in /<augmentation_type>/ folder
        #      insert [rgb_file, depth_file, augmentation_type] into list
        # else:
            # continue
    # Save [rgb_file, depth_file] list to s
        
                 


if __name__ == "__main__":
    copy_images()