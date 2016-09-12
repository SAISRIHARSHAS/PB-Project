/**
  * Created by Avinash on 9/8/2016.
  */

import org.apache.spark.{SparkContext, SparkConf}
object wordcount {
  def main(args: Array[String]) {
    System.setProperty("hadoop.home.dir", "E:\\winutils");
    val sparkConf = new SparkConf().setAppName("SparkWordCount").setMaster("local[*]")
    val sc = new SparkContext(sparkConf)
    val input = sc.textFile("C:\\Users\\Avinash\\Desktop\\tweet_p1")
    val wc=input.flatMap(line=>{line.split(" ")}).map(word=>(word,1)).cache()
    val output=wc.reduceByKey(_+_).sortByKey()
    output.saveAsTextFile("C:\\Users\\Avinash\\Desktop\\Output1")
    val o=output.collect()
    var s:String="Words:Count \n"
    o.foreach{case(word,count)=>{
      s+=word+" : "+count+"\n"
    }}
    //println(s)
  }
}