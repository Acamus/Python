package com.python.dataset;

import java.util.Random;

public class MasterDataSet {
	public static void main(String[] args) {
		System.out.println("________________________________________________________");
		System.out.println("Customer ID" + "\t\t\t" + "Customer Salary");
		System.out.println("________________________________________________________|");
		int CustID = 2546001;
		System.out.println("\t\t" + "Low Salary");
		System.out.println("________________________________________________________|");
		// for loop to generate Low salary for 30% of Customer
		for (int i = 1; i <= 30; i++) {
			Random random = new Random();
			int LowSal = random.nextInt(500000 - 120000) + 120000;
			System.out.println((CustID++) + "\t\t|\t\t" + LowSal + "\t\t\t|");
		}
		System.out.println("____________________________________________________");
		System.out.println("\t\t" + "medium Salary");
		System.out.println("____________________________________________________");
		// for loop to generate Medium salary for 40% of Customer
		for (int j = 1; j <= 40; j++) {
			Random random = new Random();
			int MedSal = random.nextInt(1000000 - 510000) + 510000;
			System.out.println((CustID++) + "\t\t|\t\t" + MedSal + "\t\t\t|");
		}
		System.out.println("_____________________________________________________");
		System.out.println("\t\t" + "High Salary");
		System.out.println("_____________________________________________________");
		// for loop to generate High salary for 30% of Customer
		for (int k = 1; k <= 30; k++) {
			Random random = new Random();
			int HighSal = random.nextInt(10000000 - 1010000) + 1010000;
			System.out.println((CustID++) + "\t\t|\t\t" + HighSal + "\t\t\t|");
		}
	}
}
