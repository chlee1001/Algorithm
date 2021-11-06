package com.ch;

import java.util.Scanner;

public class boj_1003 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int t = sc.nextInt();

    int[][] dp = new int[42][2];
    dp[0][0] = 1;
    dp[0][1] = 0;
    dp[1][0] = 0;
    dp[1][1] = 1;

    for (int i = 2; i < 41; i++) {
      dp[i][0] = dp[i - 1][0] + dp[i - 2][0];
      dp[i][1] = dp[i - 1][1] + dp[i - 2][1];
    }

    for (int i = 0; i < t; i++) {
      int n = sc.nextInt();
      System.out.println(dp[n][0] + " " + dp[n][1]);
    }
  }
}
