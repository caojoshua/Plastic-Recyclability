# Data
Data sources can be found in `data sources.txt` in the root directory. There were a total of ~8,500 images in the dataset, comprising of 
~400 MB. Each image is given a label `0 = recyclable` or `1 = non-recyclable`. I chose to only have these two labels instead of detecting the specific object just to simplify the engineering process.
## Data format
Each image was resized to 100x100 pixels and compressed into binary files in `/data/batches`. Each image is stored as 100x100x3 bytes (100 width/height, 3 colors), where each bytes represents the strength of the RGB value. Labels are stored into `/data/batches/labels.bin`, where each label is one byte. The Nth image is associated with the Nth label. Image binaries were separted into batches to accomodate github's single file max size limitation.  
I stored the images in binary files just to decrease the number of files on my system, but it is probably preferable to store in raw jpg format because of its data compressing specification. 
I originally stored images in csv format, as done in `img_to_txt.py`, but the dataset became too large, motivating me to store the dataset in binary format.
## Data scraping/reformatting process
1. Pulling data
    * Data from the github repo sources and image-net were directly downloaded. 
    * Data from google images were downloaded in the follow steps. 
      1. `google_images_url_extract.js` stores all the image URLs into a text file and downloads them into the local file system. This part requires the user to open google images, search for the desired object, scroll down to load all the images into the DOM, and then copy and paste the script into the console. Huge bust.
      2. `url_download.py` reads the URLs from the saved text file from `google_images_url_extract.js` and downloads the images to the local filesystem in `images/<search object>/<image name>`, where search object might be something like a water bottle. 
    * NOTE: this is NOT the best way to scrape from google images, as it requires manual efforts. The best way is to use a dynamic scraper such as https://github.com/zotbins/Google-Images-Scraper.
2. Reformatting data
    * `img_to_bin.py` resizes all of the images in `images/` and writes them to binary files in `batches`. Their associated labels are written to `batches/labels.bin`. Each `<search object>` is hardcoded as either a recyclable or non-recyclable. 
      
