/**
 * PROBLEM
tl;dr: Given a string of digits S, insert a minimum number of opening and closing 
parentheses into it such that the resulting string is balanced and each digit d is 
inside exactly d pairs of matching parentheses.

Let the nesting of two parentheses within a string be the substring that occurs 
strictly between them. An opening parenthesis and a closing parenthesis that is 
further to its right are said to match if their nesting is empty, or if every 
parenthesis in their nesting matches with another parenthesis in their nesting. 
The nesting depth of a position p is the number of pairs of matching parentheses 
m such that p is included in the nesting of m.

For example, in the following strings, all digits match their nesting depth: 
0((2)1), (((3))1(2)), ((((4)))), ((2))((2))(1). The first three strings have 
minimum length among those that have the same digits in the same order, but 
the last one does not since ((22)1) also has the digits 221 and is shorter.

Given a string of digits S, find another string S', comprised of parentheses 
and digits, such that:
all parentheses in S' match some other parenthesis,
removing any and all parentheses from S' results in S,
each digit in S' is equal to its nesting depth, and
S' is of minimum length.

 * INPUT
The first line of the input gives the number of test cases, T. 
T lines follow. Each line represents a test case and contains only the string S.

 * OUTPUT
For each test case, output one line containing Case #x: y, 
where x is the test case number (starting from 1) and y is the string S' 
defined above.
 */


/**
 * SOLUTION
 * Hardcode the first character with brackets, then for every character,
 * Compare it to the previous alphabet
 * If it's equal - add beside the previous alphabet 
 * If it's less - calculate the difference and skip 'difference' closing 
 *    brackets before adding it
 * If it's greater - calculate the difference and add 'difference' bracket
 *    pairs to the alphabet before adding it beside the
 *    previous alphabet
 * 
 * 
 */
object nestingDepth extends App { // Replace object name as Solution when submitting.
  
  override def main(args: Array[String]) = {

    val testCases = scala.io.StdIn.readInt()
    var res = new Array[String](testCases)
  
    // Each testcase
    for(i <- 0 until testCases) {
      
      val str = scala.io.StdIn.readLine()
      
      // Hardcoding the first value
      val first = str(0)
      res(i) = ( "(" * first.asDigit ) + "" + first + (")" * first.asDigit)
      
      // Storing first value, and will keep incrementing to the next alphabet
      // each iteration
      var previous = first
      var previousValue = previous.asDigit
      var previousIndex = res(i).indexOf(previous)
      
      
      // For Each char (aside from the 1st one which is hardcoded above)
      // For detailed explanation, check the SOLUTION comment above.
      for(char <- str.tail) {
        val value = char.asDigit
        
        // If equal
        // Inner if else added to prevent indexOutOfBounds Error
        if(previousValue == value) {
          if(res(i).length() - previousIndex == 1)
            res(i) = res(i) + value
          else 
            res(i) = res(i).substring(0, previousIndex+1) + "" + value + "" + res(i).substring(previousIndex+1, res(i).length)
        }
        // If currentValue < previousValue
        // Inner if else added to prevent indexOutOfBounds Error
        else if(previousValue > value) {
          
          val difference = previousValue - value

          if(res(i).length() - (previousIndex+difference) == 1)
            res(i) = res(i).substring(0, previousIndex + difference+1) + value
          else
            res(i) = res(i).substring(0, previousIndex + difference+1) + value + res(i).substring(previousIndex+difference+1, res(i).length) // 2nd half was previousIndex+difference not +1
        }
        
        // If previousValue < value 
        // Inner if else added to prevent indexOutOfBounds Error
        else { 
          val difference = value - previousValue
          val temp = ( "(" * difference ) + "" + value + "" + ( ")" * difference )

          if(res(i).length() - previousIndex == 1)
            res(i) = res(i) + temp
          else
            res(i) = res(i).substring(0, previousIndex+1) + temp + res(i).substring(previousIndex+1, res(i).length)
        }
          
        // Make the current alphabet as the previous alphabet before incrementing 
        previous = char
        previousValue = previous.asDigit
        previousIndex = res(i).indexOf(previous, previousIndex+1)
      }
    }
    
    // Final Output
    for(i <- 0 until res.length) {
      println("Case #" + (i+1) + ": " + res(i))
    }
  }
}
