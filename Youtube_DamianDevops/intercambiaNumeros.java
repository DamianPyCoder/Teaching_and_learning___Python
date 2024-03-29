public class intercambiaNumeros{
    public static void main(String[] args){

        int num1 = 10;
        int num2 = 20;

        //opción menos eficiente
        // int num3 = 0;   
        // num3 = num1;
        // num1 = num2;
        // num2 = num3;

        //opción más eficiente
        num1 = num1 + num2; 
        num2 = num1 - num2;
        num1 = num1 - num2;

        System.out.println("El número uno ahora es: "+num1);
        System.out.println("El número dos ahora es: "+num2);
           



    }
}