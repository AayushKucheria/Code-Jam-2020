/**
 * PROBLEM
Cameron and Jamie's kid is almost 3 years old! However, even though the child 
is more independent now, scheduling kid activities and domestic necessities 
is still a challenge for the couple.

Cameron and Jamie have a list of N activities to take care of during the day. 
Each activity happens during a specified interval during the day. They need 
to assign each activity to one of them, so that neither of them is 
responsible for two activities that overlap. An activity that ends at time t 
is not considered to overlap with another activity that starts at time t.

For example, suppose that Jamie and Cameron need to cover 3 activities: one 
running from 18:00 to 20:00, another from 19:00 to 21:00 and another from 
22:00 to 23:00. One possibility would be for Jamie to cover the activity 
running from 19:00 to 21:00, with Cameron covering the other two. Another 
valid schedule would be for Cameron to cover the activity from 18:00 to 
20:00 and Jamie to cover the other two. Notice that the first two activities 
overlap in the time between 19:00 and 20:00, so it is impossible to assign 
both of those activities to the same partner.

Given the starting and ending times of each activity, find any schedule that 
does not require the same person to cover overlapping activities, or say that 
it is impossible.

 * INPUT
The first line of the input gives the number of test cases, T. 
T test cases follow. Each test case starts with a line containing a single 
integer N, the number of activities to assign. Then, N more lines follow. 
The i-th of these lines (counting starting from 1) contains two integers Si 
and Ei. The i-th activity starts exactly Si minutes after midnight and ends 
exactly Ei minutes after midnight.

 * OUTPUT
For each test case, output one line containing Case #x: y, where x is the 
test case number (starting from 1) and y is IMPOSSIBLE if there is no valid 
schedule according to the above rules, or a string of exactly N characters 
otherwise. The i-th character in y must be C if the i-th activity is 
assigned to Cameron in your proposed schedule, and J if it is assigned to 
Jamie.
 */

/**
 * SOLUTION
 * For each activity, check if Cameron is free
 * 	If yes, assign Cameron the activity
 * If not, check if Jamie is free,
 * If yes, assign Jamie the Activity
 * If both aren't free, then don't add the activity which would lead 
 * to the IMPOSSIBLE return value later.
 * 
 * After assigning all the activities, check if the number of activities
 * assigned is equal to the total number of activities
 * If yes, return the corresponding strings with C or J
 * If no, return "IMPOSSIBLE"
 */
object Solution extends App {
  
  override def main(args: Array[String]) = {
    
    val testCases = scala.io.StdIn.readInt()
    var result = new Array[String](testCases)
    
    // Run testcases
    for(i <- 0 until testCases) {
      val activities = scala.io.StdIn.readInt()
      var timings = new Array[(Int, Int)](activities)
      var initial = new Array[(Int, Int)](activities)
      
      // Store activity times as (startTime, endTime)
      for(unit <- 0 until activities) {
        val temp = scala.io.StdIn.readLine().split(" ").map(_.trim()).map(a => a.toInt)
        timings(unit) = (temp(0), temp(1))
      }
      
      // Save the initial state
      initial = timings
      
      timings = timings.sortBy{case (start, end) => start}
      
      // Will store the timings of activities that each one will do
      var cameron: List[(Int, Int)] = List()
      var jamie: List[(Int, Int)] = List()

      // For each activity
      for(unit <- timings) {
        if(cameron.isEmpty) {
          cameron = cameron :+ unit
        }
        // If Cameron's last activity finishes before this one starts
        else if(cameron.last._2 <= unit._1) {
          cameron = cameron :+ unit
        }
        else if(jamie.isEmpty) {
          jamie = jamie :+ unit         
        }
        // If Jamie's last activity finishes before this one starts
        else if(jamie.last._2 <= unit._1) {
          jamie = jamie :+ unit
        }
      }
      
      // If all the activities have been divided, this should be true
      if(cameron.length + jamie.length == initial.length) {
        var tempRes: String = ""
        
        // For each activity, check if Cameron or Jamie contain the activity,
        // If yes, edit the result accordingly and remove that activity
        // from Jamie/Cameron's list.
        for(elem <- initial) {
          if(cameron.contains(elem)) {
            tempRes += "C"
            cameron = cameron.filter{case (start, end) => (start != elem._1) && (end != elem._2)}
          }
          else if(jamie.contains(elem)) {
            tempRes += "J"
            jamie = jamie.filter{case (start, end) => (start != elem._1) && (end != elem._2)}
          }
          else tempRes += "?"
        }
        result.update(i, tempRes)
      }
      else result.update(i, "IMPOSSIBLE")
    }
    
    // Final Output
    for(i <- 0 until result.length) {
      println("Case #" + (i+1) + ": " + result(i))
    }
  }
    
  
}