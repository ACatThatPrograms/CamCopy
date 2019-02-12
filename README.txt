Cam Copy V 1.0.0

This program's purpose is to copy both raw and compressed picture formats from a source directory to a target directory easily.

Please pay attention to notes designated with an asterisk if your camera seperates your RAW and Compressed types to different folders.

--Quick Start--

1. Start Script. ( python ./CamCopy.py )

2. Script will greet you and begin configuration for your camera if it has not yet been set.
Configuration is not case sensitive and will handle file extension periods.

3. Use 'check' command to verify your configuration went smoothly, if not run the 'config' command
After your configuration is set it will be remembered in CamCopy.conf

You can use 'checkfile' to view the contents of CamCopy.conf at any time, though it is a debug command and not necessary.

4. After configuration use the 'add' command to start the file add guide.

Please note if you have already created a list adding will append them to the existing list, 
If you would like to start with a new list issue the 'clearlist' command.

5. Follow onscreen prompts from the 'add' command to add selected file to the List.

6. The list is a collection of files you want copied.
CamCopy will automatically append the correct extensions to the file types when you go to copy them.

If you execute the 'list' command you will see the files you added.

Two files will be created and keep track of your list
rawlist.dat and imglist.dat, rawlist is viewable if desired with the debug command 'rawlist' but it is not necessary.

imglist.dat is the serialization of the user friendly list of files.
rawlist.dat is the serialization that contains all possible iterations of the file name to control case sensitivity of operating systems.

7. After your files have been added to The List, you can begin the copy sequence by using the 'copy' command to start the process.

8. You will be asked for the source and target location for your files.
If CamCopy has any issues finding the directories it will let you know.

Please note CamCopy will not issues notices on files that are not found that are within your list.
Due to the nature of CamCopy's file copying process it will merely skip the file instead.
A feature to check for the files may be implemented in the future if interest is shown.

You will be asked to verify the source and target before copying begins.

Copying is done verbosely and CamCopy will let you know when it is finished.

**If your camera keeps raw and compressed images in seperate directories**
Run this command again in the other directory to achieve the same results.

9. Your list will be saved for future use if you need it again, however if you don't need it anymore you can clear it with the 'clearlist' command.

It is advised on start-up to run the clearlist command unless you have a specific need to copy the same files again.

--Advanced Commands--

CamCopy can also be used to copy files of any combination type or single type. e.g music Track1.wav Track1.mp3 or just Track2.mp3

Due to the way CamCopy handles file processing it will just pass over any files that aren't found.

If you are copying files that do not have a prefix like camera files, you may use the command delprefx to remove the
prefix that is applied to your files when they are added. Note that this does not remove the prefix from existing files in The List.

--Legalese--

CamCopy is completely open source under an...

