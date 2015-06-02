import os

##### Specify file path #####
# output = file path of output for pilercr reports
# genomePath = file path of genome, function will look for spacers in this genome, FASTA format

pilerOut = "crispr-crt/%s"
genomePath = "genomes/"
number_of_files = len([name for name in os.listdir(genomePath)])
i = 1

##### Find CRISPR using pilercr #####
for fn in os.listdir(genomePath):
    print "Generating report %i out of %i" % (i, number_of_files)
    cmd = "java -cp /vagrant/Tools/CRT1.2-CLI.jar crt %s %s"%(genomePath + fn,pilerOut % fn)
    os.system(cmd + "> /dev/null 2>&1") 
    i += 1
