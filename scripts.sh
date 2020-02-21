#list the names of files in the archive
#adding "v" to option increases verbosity (ls -l type output)

tar -ztf repository_metadata_2013-04-12.tar.gz

#selectively extract file
# again "-v" for verbose, it gives an indication of the file being successfully extraction
tar -zvxf repository_metadata_2013-04-12.tar.gz repository_metadata_9_2013-03-18.json

#grep