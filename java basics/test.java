import java.util.Scanner;

class test2
{
    public static void main(String[] args)
    {
        System.out.println("Hello World");
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter element space separated ");
        String[] arr = sc.nextLine().split(" ");    // input: 1 2 3 4 5
        int n = arr.length;
        int[] arr1 = new int[n];
        for (int i=0; i<n; i++)
        {
            arr1[i] = Integer.parseInt(arr[i]);
        }
        for (int i=0; i<n; i++)
        {
            System.out.print(arr1[i] + " ");
        }
        sc.close();
    }
}