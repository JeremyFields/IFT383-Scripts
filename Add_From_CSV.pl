#!/usr/bin/perl

# loop through entire file
while(<>){

   # chomp $_
   chomp;
   # do not need to include string, will work on $_
   @nums = split(/,/);

   # loop through array and sum numbers
   foreach $numbers (@nums){
      $sum += $numbers;
   }
}

# print the sum and a new line
print "$sum\n";
