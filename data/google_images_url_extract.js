
	path = "C:\Users\caojo\Desktop\plastic dataset\scripts";
	file = "plastic_bag.txt"

	var imgs=document.getElementsByTagName("a");
	var i=0;
	var aray=new Array();var j=-1;
	var str = "";

	// const fs = require('fs');

	while(++i<imgs.length){
		if(imgs[i].href.indexOf("/imgres?imgurl=http")>0){
			str += decodeURIComponent(imgs[i].href).split(/=|%|&/)[1].split("?imgref")[0] + "\n";
		}
	}



    var textToWrite = str;
    var textFileAsBlob = new Blob([textToWrite], {type:'text/plain'});
    var fileNameToSaveAs = "urls";
      var downloadLink = document.createElement("a");
    downloadLink.download = fileNameToSaveAs;
    downloadLink.innerHTML = "Download File";
    if (window.webkitURL != null)
    {
        // Chrome allows the link to be clicked
        // without actually adding it to the DOM.
        downloadLink.href = window.webkitURL.createObjectURL(textFileAsBlob);
    }
    else
    {
        // Firefox requires the link to be added to the DOM
        // before it can be clicked.
        downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
        downloadLink.onclick = destroyClickedElement;
        downloadLink.style.display = "none";
        document.body.appendChild(downloadLink);
    }

    downloadLink.click();

