package com.sc;

import java.util.HashMap;
import java.util.Random;

/** Generate 10 random integers in the range 0..99. */
public final class qwert {
  
  public static final void main(String... aArgs){
    log("Generating 10 random integers in range 0..99.");
    
    //note a single Random object is reused here
    Random randomGenerator = new Random();
    for (int idx = 1; idx <= 40; ++idx){
     // int randomInt = randomGenerator.nextInt(1000000-510000)+510000;
    	 int randomInt = randomGenerator.nextInt(10000000-1000000)+1000000;
      int month = randomInt/12;
      System.out.println(month);
      //log("Generated : " + month);
    }
    
    log("Done.");
  }
  
  private static void log(String aMessage){
    System.out.println(aMessage);
  }
}