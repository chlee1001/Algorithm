package com.ch;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class boj_1008 {
  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    String input = bf.readLine();
    StringTokenizer st = new StringTokenizer(input, " ");

    Double a = Double.parseDouble(st.nextToken());
    Double b = Double.parseDouble(st.nextToken());
    System.out.println(a / b);
  }
}
