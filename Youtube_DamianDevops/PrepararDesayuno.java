public class PrepararDesayuno {
    public static void main(String[] args){

        TareaSandwich tareaSandwich = new TareaSandwich();
        TareaZumo tareaZumo = new TareaZumo();

        Thread hiloSandwich = new Thread(tareaSandwich);
        Thread hiloZumo = new Thread(tareaZumo);

        hiloSandwich.start();
        hiloZumo.start();

        try{
            hiloSandwich.join();
            hiloZumo.join();
        } catch (InterruptedException e){
            System.out.println("ERROR: Se interrumpió la ejecución del hilo");
        }
        System.out.println("Bon apetit, desayuno listo!");
    }
}
class TareaSandwich implements Runnable{
    public void run(){
        System.out.println("Preparando el sandwich...");
        try{
            Thread.sleep(4000);
        } catch (InterruptedException e){
            System.out.println("No se ha podido terminar de preparar el sandwich");
        }
        System.out.println("¡Listo el sandwich!");
    }
}
class TareaZumo implements Runnable{
    public void run(){
        System.out.println("Preparando el zumo...");
        try{
            Thread.sleep(2000);
        } catch (InterruptedException e){
            System.out.println("No se ha podido terminar de preparar el zumo");
        }
        System.out.println("¡Listo el zumo!");
    }
}
