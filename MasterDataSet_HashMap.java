package com.python.dataset;

import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Random;

public class MasterDataSet {
	
	public static void main(String[] args) {
		LinkedHashMap<Integer, Integer> linkedHashMap=new LinkedHashMap<Integer, Integer>();
		System.out.println("________________________________________________________");
		System.out.println("Customer ID" + "\t\t\t" + "Customer Salary");
		System.out.println("________________________________________________________|");
		System.out.println("\t\t" + "Low Salary");
		System.out.println("________________________________________________________|");
		// for loop to generate Low salary for 30% of Customer
		for (int i = 2546001; i <= 2546030; i++) {
			Random random = new Random();
			int LowSal = random.nextInt(500000 - 120000) + 120000;
			System.out.println((i) + "\t\t|\t\t" + LowSal + "\t\t\t|");
			linkedHashMap.put(i, (LowSal/12));
		}
		System.out.println("____________________________________________________");
		System.out.println("\t\t" + "medium Salary");
		System.out.println("____________________________________________________");
		// for loop to generate Medium salary for 40% of Customer
		for (int j = 2546031; j <= 2546070; j++) {
			Random random = new Random();
			int MedSal = random.nextInt(1000000 - 510000) + 510000;
			System.out.println((j) + "\t\t|\t\t" + MedSal + "\t\t\t|");
			linkedHashMap.put(j, (MedSal/12));
		}
		System.out.println("_____________________________________________________");
		System.out.println("\t\t" + "High Salary");
		System.out.println("_____________________________________________________");
		// for loop to generate High salary for 30% of Customer
		for (int k = 2546071; k <= 2546100; k++) {
			Random random = new Random();
			int HighSal = random.nextInt(10000000 - 1010000) + 1010000;
			System.out.println((k) + "\t\t|\t\t" + HighSal + "\t\t\t|");
			linkedHashMap.put(k, (HighSal/12));
		}
		for(Map.Entry m:linkedHashMap.entrySet()){
			System.out.println(m.getKey()+"   "+m.getValue());
		}
		
	}
}
