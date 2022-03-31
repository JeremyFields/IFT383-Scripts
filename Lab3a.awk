BEGIN {
   FS=","

   # print the header
   print "Name\t Low\t High\t Average"
}

{
   if(FNR!=1){

      # create an array "high" with each assignment as the index
      # go row by row and compare scores, if current score is lower
      # reassign value to $4 (the higher score)
      if(high[$3] < $4){
         high[$3] = $4
      }

      # create an array "low" with each assignment as the index
      # go row by row and compare scores, if current score is higher
      # reassign value to $4 (the lower score)
      if(low[$3] > $4 || low[$3] == 0){
         low[$3] = $4
      }
      # create an array "sum" to add total of each assignment
      # create an array "count" to get quantity of each assignment
      sum[$3] += $4
      count[$3] += 1

   }
}

END {
   # loop through each assignment
   for(assgn in low){
      # calculate average (sum of assignment scores / quantity of assignment)
      avg[assgn] = sum[assgn] / count[assgn]
      # print assignment name, low score, high score, average
      printf "%-5s\t %-2d\t %-5d\t %-8.2f\n", assgn, low[assgn], high[assgn], avg[assgn]
   }
   printf "\n"
}
