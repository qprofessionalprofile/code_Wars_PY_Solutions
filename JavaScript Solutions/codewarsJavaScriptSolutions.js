/* 
Codewars solutions

No names from the Katas will be given, but I will be showing my solutions-
and thought processes. 
*/


//Filtering lists

function gooseFilter (birds) {
  var geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"];
  let filteredBirds = [];
 
  for (let i=0; i< birds.length; i++){
    if (!geese.includes(birds[i])){
      filteredBirds.push(birds[i])
    }
  }
  return filteredBirds
};

/* 
use the defined function and list  and filter through to remove the birds
assign an empty list of filtered birds
loop through the list and start the list at the 0 index 
check the lists index of the birds and check the length of birds to go through the iterations
look through and check to make sure that if the list doesnt contain geese in birds using the includes function -
then if it doesn't then push it to the empty list. 
return the list
*/