package com.ch;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class boj_1009 {
  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    int t = Integer.parseInt(bf.readLine());

    for (int i = 0; i < t; i++) {
      String input = bf.readLine();
      StringTokenizer st = new StringTokenizer(input, " ");
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());

      ArrayList<Integer> resultList = new ArrayList<>();

      for (int j = 0; j < 4; j++) {
        resultList.add(j, (int) (Math.pow(a, (j + 1)) % 10));
      }
      int pos = b % 4 - 1;
      if (pos < 0) {
        pos += 4;
      }
      int result = resultList.get(pos);
      if (result != 0) {
        System.out.println(result);
      } else {
        System.out.println(10);
      }

    }
  }
}
