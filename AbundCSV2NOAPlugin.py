import sys

class AbundCSV2NOAPlugin:
   def input(self, inputfile):
      csvfilename = inputfile
      csvfile = open(csvfilename, 'r')
      # Read entire abundance file first
      firstline = csvfile.readline()
      self.bacteria = firstline.split(',')
      self.bacteria.remove(self.bacteria[0])
      self.abund = []
      for i in range(len(self.bacteria)):
         self.abund.append(0)
      self.numreads = 0
      for line in csvfile:
         self.numreads += 1
         contents = line.split(',')
         for i in range(1, len(self.bacteria)):
            self.abund[i-1] += float(contents[i])

   def run(self):
      pass

   def output(self, outputfile):
      noafilename = outputfile
      noafile = open(noafilename, 'w')
      noafile.write("Name"+"\t"+"Abundance"+"\n")

      i = 0
      minabund = 1
      maxabund = 0
      sumabund = 0

      for bacterium in self.bacteria:
         bac = bacterium.strip()
         avg = self.abund[i-1] / self.numreads
         noafile.write(bac[1:len(bac)-1]+"\t"+str(avg)+"\n")
         if (avg > maxabund):
            maxabund = avg
         if (avg < minabund):
            minabund = avg 
         sumabund += avg
         i += 1

      print ("Min Abundance: "+str(minabund))
      print ("Max Abundance: "+str(maxabund))
      print ("Avg Abundance: "+str(float(sumabund) / i))
