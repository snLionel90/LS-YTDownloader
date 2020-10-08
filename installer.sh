echo "MENU"
echo "1. Download LS-Youtube Downloader and Install APT Components"
echo "2. Update Repository List"
echo "Choose one option: "
read opcion
convert=false
if [ "$opcion" = 1 ]; then
        echo "****Installing PYTHON 3****"
        sudo apt-get install python3
        echo ""
        echo ""
        echo "****Installing LS-YT DOWNLOADER****"
        sudo git clone https://github.com/snLionel90/LS-YTDownloader.git
        echo ""
        echo ""
        echo "****Installing PIP 3****"
        sudo apt-get install python3-pip -y
        echo ""
        echo ""
        echo "****Updating LS-YOUTUBE-DL****"
        sudo pip3 install --upgrade youtube-dl
        echo ""
        echo ""
        echo "****Installing TKINTER****"
        sudo apt-get install python3-tk -y
        echo ""
        echo ""
        echo "****Installing FFMPEG Libraries****"
        sudo apt-get install ffmpeg -y
        echo ""
        echo ""
        clear
        convert=true

elif [ "$opcion" = 2 ]; then
        echo "Updating repository list"
        sudo apt-get update
else
        echo "Failure,script doesn't work properly, closing"
fi

if [ "$convert" = true ]; then
        echo "####################################### END #######################################"
        echo "Para ejecutar la aplicacion, tan solo tienes que escribir YTDownloader.py"
        echo "##########################################################################################$
fi

