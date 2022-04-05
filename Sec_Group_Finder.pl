#!/usr/bin/perl

# print title
print "List of Security Groups: \n\n";

# loop through file
while(<>){
   # create an array, split file by new line character
   @groups = split("\n");

   # loop through the array
   foreach $set(@groups){
      # retrieve the index where the comma first appears, save in variable
      $index = index($set, ',');

      # check for each index, each line has a verying index where
      # the comma appears,  so we need to locate
      # appropriate lines for use with substr
      if($index == 16){
         print substr($set, 3, 13);
         print "\n";
      }
      elsif($index == 13){
         print substr($set, 3, 10);
         print "\n";
      }
      elsif($index == 19){
         print substr($set, 3, 16);
         print "\n";
      }
      else{
         print substr($set, 3, 12);
         print "\n";
      }
   }
}
