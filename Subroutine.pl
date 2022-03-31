#!/usr/bin/perl

sub addAll {
   my $TOTAL=0;

   # Loop through passed arguments in @_ array
   #  and add to get the total
   foreach $num(@_){
      $TOTAL += $num;
   }

   # return sum of arguments
   return $TOTAL;
}

# Test by passing any number of arguments
print addAll(1, 2, 3, 4, 5) . "\n";
print addAll(5, 10, 0, 1) . "\n";
print addAll(1,1) . "\n";
