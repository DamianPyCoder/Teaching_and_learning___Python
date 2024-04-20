import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Deque;
import java.util.HashMap;
import java.util.TreeMap;
import java.util.LinkedHashMap;

import javax.swing.plaf.basic.BasicInternalFrameTitlePane.SystemMenuBar;

public class Tipos {
    public static void main(String[] args) {

            System.out.println("");
            System.out.println("");
            
            // NÚMEROS
            // float numeroFloat = 3.3;
            // double numeroDouble = 4.4;

            // byte numberByte =0; // -128 hasta 127
            // short numberShort = 2; //-32.768 hasta 32.767
            // int numberInt= 3; //- 2.147.483648 hasta 2.147.483647
            // long numberLong = 4; //- 9 trillones hasta 9 trillones


            
            // ARRAY
            // int[] numeros = new int[5];
            // //_ _ _ _ _
            // numeros[0] = 1;
            // numeros[1] = 2;
            // numeros[2] = 3;
            // numeros[3] = 4;
            // numeros[4] = 5;
            // System.out.println("El primer valor del array es: "+numeros[0]);
            // System.out.println("El último valor del array es: "+numeros[4]);

            // for (int i = 0; i< numeros.length; i++){
            //     System.out.println("Posición "+i+": "+numeros[i]);
            // }

            // // Python List
            // numerosPy = [1,2,3,4,5]
            // print("El primer número es: ", numerosPy[0]);
            // for i in ranger(len(numerosPy)):
            //     print("Posición ",i,";",numerosPy[i]);

            // numeros[2] = 12;
            // int[] copiaArray = Arrays.copyOf(numeros, numeros.length );

            // int indice = -1;
            // for (int i = 0; i <numeros.length; i++){
            //     if (numeros[i] == 12){
            //         indice = i;
            //         break;
            //     }
            // }
            // if (indice >= 0){
            //     System.out.println("El valor de 12 se encuentra en el indice: "+indice);
            // } else {
            //     System.out.println("El valor indicado no se encuentra en el array");
            // }


            // ARRAYLIST

            // ArrayList<Integer> numeros = new Arraylist<>();

            // numeros.add(1);
            // numeros.add(12);
            // numeros.add(32);

            // numeros.add(1,18);
            
            // int longitud =numeros.size();

            // int valor = numeros.get(0);

            // numeros.set(2, 44);

            // numeros.remove(1);

            // numeros.remove(Integer.valueOf(32));

            // boolean esta= numeros.contains(12);
            
            // numeros.clear();

            // boolean vacio = numeros.isEmpty();

            // ArrayList<Integer> copiaNumeros = new ArrayList<>(numeros);

            // Integer[] array = numeros.toArray(new Integer[numeros.size()]);

            // int indice = numeros.indexOf(32);

            // int ultimoIndice = numeros.lastIndexOf(32);




            // // LINKEDLIST
            // //  NODO ANTERIOR -   NODO     - NODO SIGUIENTE         /    NODO ANTERIOR - NODO 2 - NODO SIGUIENTE
            // LinkedList<Integer> lista = new LinledList<>();
            // lista.add(1);
            // lista.add(2);

            // lista.add(1,4);
            // lista.addFirst(6);
            // lista.addLast(43);
            // lista.getFirst();
            // lista.getLast();
            // lista.removeFirst();
            // lista.removeLast();
            // lista.remove(Integer.valueOf(43));
            // lista.remove(2);
            // boolean contiene = lista.contains(12);
            // lista.size();
            // lista.clear();
            // int elemento = lista.get(3);
            // lista.set(3,65);
            // lista.indexOf(32);
            // lista.lastIndexOf(32);
            // lista.isEmpty();
            // Integer[] array = lista.toArray(new Integer[lista.size()]);

            // Deque<Integer> stack = new LinkedList<>();

            // stack.push(1);
            // stack.push(2);
            // stack.push(3);
            
            // System.out.println("Primer elemento: "+stack.peek());
            // while(!stack.isEmpty()){
            //     System.out.println("ELemento eliminado: "+stack.pop());
            // }
            
            // stack.isEmpty();
            // stack.size();
            // stack.clear();
            // Deque<Integer> stackSegundo = new LinkedList<>(stack);
            // Iterator<Integer> iterador = stack.iterator();
            // boolean contiene = stack.contains(3);
            // stack.removeAll(Collections.singleton(12));
            // stack.removeIf(relemento -> elemento % 2 == 0);
            // List<Integer> lista = new ArrayList<>(stack);
            // Object[] copiaArray = stack.toArray();
            // stack.addAll(otroStack);
            // stack.AddAll(0,otroStack);
            // boolean coneieneTodos = stack.containsAll(otroStack);
            // stack.removeAll(otroStack);
            // stack.retainAll(otroStack);
            // stack.peek();
            // stack.pop();
            // while(stack.peek() != 10){ stack.pop();}
            // while (stack.indexOf(19) != 0){ stack.pop();}
            // stack.removeLast();
            // Iterator<Integer> iteradorInverso = stack.descendingIterator();
            // Deque<Integer> subStack = new LinkedList<>(stack.subList(2, stack.size()));
            // stack.indexOf(3);
            // stack.lastIndexOf(3);



            // TREEMAP, HASHMAP, LINKEDHASHMAP
            // TREEMAP

            // TreeMap<String, Integer> treeMap = new TreeMap<>();
            // treeMap.put("A",1);
            // treeMap.put("B",2);
            // treeMap.put("C",3);

            // int valor = treeMap.get("A");
            // for (String clave : treeMap.keySet()){
            //     System.out.println("clave: "+clave+" , valor: "+treeMap.get(clave));
            // }

            // // HASHMAP
            // HashMap<String, Integer> HashMap = new HashMap<>();
            // hashMap.put("A",1);
            // hashMap.put("B",2);
            // hashMap.put("C",3);
            // int valorHash = hashMap.get("A");
            // for (String clave : hashMap.keySet()){
            //     System.out.println("clave: "+clave+" , valor: "+hashMap.get(clave));
            // }


            // // LINKEDHASHMAP
            // LinkedHashMap<String, Integer> linkedHashMap = new LinkedHashMap<>();
            // linkedHashMap.put("A",1);
            // linkedHashMap.put("B",2);
            // linkedHashMap.put("C",3);
            // int valorLkp = linkedHashMap.get("A");
            // for (String clave : linkedHashMap.keySet()){
            //     System.out.println("clave: "+clave+" , valor: "+linkedHashMap.get(clave));
            // }


            // TREEMAP funciones
            // Crear un TreeMap
            // TreeMap<Integer, String> treeMap = new TreeMap<>();
    
            // treeMap.put(1, "Uno");
            // treeMap.put(2, "Dos");
            // treeMap.put(3, "Tres");
    
            // String valor = treeMap.get(1);
            // System.out.println("Valor asociado a la clave '1': " + valor);
    
            // boolean contieneClave = treeMap.containsKey(2);
            // System.out.println("¿Contiene la clave '2'?: " + contieneClave);
    
            // boolean contieneValor = treeMap.containsValue("Cuatro");
            // System.out.println("¿Contiene el valor 'Cuatro'?: " + contieneValor);
    
            // int primeraClave = treeMap.firstKey();
            // String primerValor = treeMap.remove(primeraClave);
            // System.out.println("Primer elemento eliminado: " + primeraClave + " -> " + primerValor);
    
            // int ultimaClave = treeMap.lastKey();
            // String ultimoValor = treeMap.remove(ultimaClave);
            // System.out.println("Último elemento eliminado: " + ultimaClave + " -> " + ultimoValor);
    
            // int tamano = treeMap.size();
            // System.out.println("Tamaño del TreeMap: " + tamano);
    
            // boolean estaVacio = treeMap.isEmpty();
            // System.out.println("¿El TreeMap está vacío?: " + estaVacio);
    
            // String mapeoRemovido = treeMap.pollFirstEntry().getValue();
            // System.out.println("Primer mapeo eliminado: " + mapeoRemovido);
    
            // mapeoRemovido = treeMap.pollLastEntry().getValue();
            // System.out.println("Último mapeo eliminado: " + mapeoRemovido);
    
            // int claveAnterior = treeMap.lowerKey(2);
            // System.out.println("Clave anterior a '2': " + claveAnterior);
    
            // int clavePosterior = treeMap.higherKey(1);
            // System.out.println("Clave posterior a '1': " + clavePosterior);
    
            // String primerMapeo = treeMap.firstEntry().getValue();
            // System.out.println("Primer mapeo: " + primerMapeo);
    
            // String ultimoMapeo = treeMap.lastEntry().getValue();
            // System.out.println("Último mapeo: " + ultimoMapeo);
    
            // System.out.println("Conjunto de claves: " + treeMap.keySet());
    
            // System.out.println("Colección de valores: " + treeMap.values());
    
            // System.out.println("Conjunto de mapeos: " + treeMap.entrySet());
    
            // treeMap.clear();
    
            // TreeMap<Integer, String> otroTreeMap = new TreeMap<>();
            // otroTreeMap.put(4, "Cuatro");
            // otroTreeMap.put(5, "Cinco");
            // treeMap.putAll(otroTreeMap);
            // System.out.println("TreeMap después de copiar otro TreeMap: " + treeMap);
    
            // treeMap.replace(4, "NuevoCuatro");
            // System.out.println("TreeMap después de reemplazar el valor asociado a '4': " + treeMap);
    
            // treeMap.replace(4, "NuevoCuatro", "ReemplazadoCuatro");
            // System.out.println("TreeMap después de reemplazar el valor asociado a '4' solo si es 'NuevoCuatro': " + treeMap);
    
            // treeMap.replaceAll((k, v) -> v.toUpperCase());
            // System.out.println("TreeMap después de reemplazar todos los valores con mayúsculas: " + treeMap);
    
            // TreeMap<Integer, String> cloneMap = (TreeMap<Integer, String>) treeMap.clone();
            // System.out.println("Clon del TreeMap: " + cloneMap);
    
            // System.out.println("Submapa del TreeMap: " + treeMap.subMap(2, 5));
    
            // System.out.println("Submapa del TreeMap hasta '4': " + treeMap.headMap(4));
    
            // System.out.println("Submapa del TreeMap desde '4': " + treeMap.tailMap(4));
    
            // System.out.println("Submapa del TreeMap entre '2' y '5': " + treeMap.subMap(2, true, 5, true));
    
            // System.out.println("Submapa del TreeMap excluyendo '4': " + treeMap.subMap(2, false, 4, false));
    
            // boolean sonIguales = treeMap.equals(otroTreeMap);
            // System.out.println("¿Son iguales los dos TreeMaps?: " + sonIguales);
    
            // int hash = treeMap.hashCode();
            // System.out.println("Hash del TreeMap: " + hash);
            

            // // Crear un HashMap
            // HashMap<Integer, String> hashMap = new HashMap<>();
    
            // // 1. Agregar elementos al HashMap
            // hashMap.put(1, "Uno");
            // hashMap.put(2, "Dos");
            // hashMap.put(3, "Tres");
    
            // // 2. Obtener el valor asociado a una clave
            // String valor = hashMap.get(1);
            // System.out.println("Valor asociado a la clave '1': " + valor);
    
            // // 3. Verificar si el HashMap contiene una clave específica
            // boolean contieneClave = hashMap.containsKey(2);
            // System.out.println("¿Contiene la clave '2'?: " + contieneClave);
    
            // // 4. Verificar si el HashMap contiene un valor específico
            // boolean contieneValor = hashMap.containsValue("Cuatro");
            // System.out.println("¿Contiene el valor 'Cuatro'?: " + contieneValor);
    
            // // 5. Obtener y eliminar el valor asociado a una clave
            // String valorEliminado = hashMap.remove(1);
            // System.out.println("Valor eliminado asociado a la clave '1': " + valorEliminado);
    
            // // 6. Obtener el tamaño del HashMap
            // int tamano = hashMap.size();
            // System.out.println("Tamaño del HashMap: " + tamano);
    
            // // 7. Comprobar si el HashMap está vacío
            // boolean estaVacio = hashMap.isEmpty();
            // System.out.println("¿El HashMap está vacío?: " + estaVacio);
    
            // // 8. Obtener una vista del conjunto de claves del HashMap
            // System.out.println("Conjunto de claves: " + hashMap.keySet());
    
            // // 9. Obtener una vista del conjunto de valores del HashMap
            // System.out.println("Colección de valores: " + hashMap.values());
    
            // // 10. Obtener una vista del conjunto de mapeos del HashMap
            // System.out.println("Conjunto de mapeos: " + hashMap.entrySet());
    
            // // 11. Eliminar todos los mapeos del HashMap
            // hashMap.clear();
    
            // // 12. Copiar todos los mapeos de otro mapa al HashMap
            // HashMap<Integer, String> otroHashMap = new HashMap<>();
            // otroHashMap.put(4, "Cuatro");
            // otroHashMap.put(5, "Cinco");
            // hashMap.putAll(otroHashMap);
            // System.out.println("HashMap después de copiar otro HashMap: " + hashMap);
    
            // // 13. Reemplazar el valor asociado a una clave con un nuevo valor
            // hashMap.replace(4, "NuevoCuatro");
            // System.out.println("HashMap después de reemplazar el valor asociado a '4': " + hashMap);
    
            // // 14. Reemplazar el valor asociado a una clave solo si coincide con un valor específico
            // hashMap.replace(4, "NuevoCuatro", "ReemplazadoCuatro");
            // System.out.println("HashMap después de reemplazar el valor asociado a '4' solo si es 'NuevoCuatro': " + hashMap);
    
            // // 15. Reemplazar el valor asociado a una clave con el resultado de una función
            // hashMap.replaceAll((k, v) -> v.toUpperCase());
            // System.out.println("HashMap después de reemplazar todos los valores con mayúsculas: " + hashMap);
    
            // // 16. Clonar el HashMap
            // HashMap<Integer, String> cloneMap = (HashMap<Integer, String>) hashMap.clone();
            // System.out.println("Clon del HashMap: " + cloneMap);
    
            // // 17. Verificar si dos HashMap son iguales
            // boolean sonIguales = hashMap.equals(otroHashMap);
            // System.out.println("¿Son iguales los dos HashMaps?: " + sonIguales);
    
            // // 18. Calcular el hash del HashMap
            // int hash = hashMap.hashCode();
            // System.out.println("Hash del HashMap: " + hash);
    
            // // 19. Obtener el valor asociado a una clave, o un valor predeterminado si la clave no está presente
            // String valorOrDefault = hashMap.getOrDefault(6, "Seis");
            // System.out.println("Valor asociado a la clave '6' o predeterminado: " + valorOrDefault);
    
            // // 20. Insertar un mapeo solo si la clave no está presente en el HashMap
            // hashMap.putIfAbsent(7, "Siete");
            // System.out.println("HashMap después de insertar '7' solo si la clave no está presente: " + hashMap);
    
            // // 21. Obtener y eliminar el valor asociado a una clave si y solo si coincide con un valor específico
            // boolean eliminado = hashMap.remove(7, "Siete");
            // System.out.println("¿Se eliminó la clave '7' con el valor 'Siete'?: " + eliminado);
    
            // // 22. Obtener y reemplazar el valor asociado a una clave con un nuevo valor
            // String valorReemplazado = hashMap.replace(5, "ReemplazoCinco");
            // System.out.println("Valor reemplazado asociado a la clave '5': " + valorReemplazado);
    
            // // 23. Obtener y reemplazar el valor asociado a una clave con un nuevo valor solo si coincide con un valor específico
            // boolean reemplazado = hashMap.replace(5, "ReemplazoCinco", "NuevoReemplazoCinco");
            // System.out.println("¿Se reemplazó el valor asociado a '5' solo si era 'ReemplazoCinco'?: " + reemplazado);
    
            // // 24. Obtener o calcular el valor asociado a una clave, y almacenarlo si no está presente en el HashMap
            // String valorComputado = hashMap.computeIfAbsent(8, k -> "ComputadoOcho");
            // System.out.println("Valor computado asociado a la clave '8': " + valorComputado);
    
            // // 25. Calcular el valor asociado a una clave y reemplazar el valor existente si está presente en el HashMap
            // String valorCalculado = hashMap.computeIfPresent(8, (k, v) -> v + " Modificado");
            // System.out.println("Valor calculado y reemplazado asociado a la clave '8': " + valorCalculado);
    
            // // 26. Calcular el valor asociado a una clave y almacenarlo en el HashMap
            // String valorCalculadoNuevo = hashMap.compute(9, (k, v) -> "ComputadoNuevoNueve");
            // System.out.println("Valor calculado y almacenado asociado a la clave '9': " + valorCalculadoNuevo);
    
            // // 27. Fusionar el valor asociado a una clave con un nuevo valor si la clave está presente en el HashMap
            // hashMap.merge(9, " Fusionado", (oldValue, newValue) -> oldValue.concat(newValue));
            // System.out.println("HashMap después de fusionar el valor asociado a '9': " + hashMap);
    
            // // 28. Obtener una vista del submapa del HashMap
            // System.out.println("Submapa del HashMap: " + hashMap.subMap(2, 5));
    
            // // 29. Obtener una vista del submapa del HashMap hasta una clave específica
            // System.out.println("Submapa del HashMap hasta '5': " + hashMap.headMap(5));
    
            // // 30. Obtener una vista del submapa del HashMap desde una clave específica
            // System.out.println("Submapa del HashMap desde '5': " + hashMap.tailMap(5));
    





            // // Crear un LinkedHashMap
            // LinkedHashMap<Integer, String> linkedHashMap = new LinkedHashMap<>();

            // // 1. Agregar elementos al LinkedHashMap
            // linkedHashMap.put(1, "Uno");
            // linkedHashMap.put(2, "Dos");
            // linkedHashMap.put(3, "Tres");

            // // 2. Obtener el valor asociado a una clave
            // String valor = linkedHashMap.get(1);
            // System.out.println("Valor asociado a la clave '1': " + valor);

            // // 3. Verificar si el LinkedHashMap contiene una clave específica
            // boolean contieneClave = linkedHashMap.containsKey(2);
            // System.out.println("¿Contiene la clave '2'?: " + contieneClave);

            // // 4. Verificar si el LinkedHashMap contiene un valor específico
            // boolean contieneValor = linkedHashMap.containsValue("Cuatro");
            // System.out.println("¿Contiene el valor 'Cuatro'?: " + contieneValor);

            // // 5. Obtener y eliminar el valor asociado a una clave
            // String valorEliminado = linkedHashMap.remove(1);
            // System.out.println("Valor eliminado asociado a la clave '1': " + valorEliminado);

            // // 6. Obtener el tamaño del LinkedHashMap
            // int tamano = linkedHashMap.size();
            // System.out.println("Tamaño del LinkedHashMap: " + tamano);

            // // 7. Comprobar si el LinkedHashMap está vacío
            // boolean estaVacio = linkedHashMap.isEmpty();
            // System.out.println("¿El LinkedHashMap está vacío?: " + estaVacio);

            // // 8. Obtener una vista del conjunto de claves del LinkedHashMap
            // System.out.println("Conjunto de claves: " + linkedHashMap.keySet());

            // // 9. Obtener una vista del conjunto de valores del LinkedHashMap
            // System.out.println("Colección de valores: " + linkedHashMap.values());

            // // 10. Obtener una vista del conjunto de mapeos del LinkedHashMap
            // System.out.println("Conjunto de mapeos: " + linkedHashMap.entrySet());

            // // 11. Eliminar todos los mapeos del LinkedHashMap
            // linkedHashMap.clear();

            // // 12. Copiar todos los mapeos de otro mapa al LinkedHashMap
            // LinkedHashMap<Integer, String> otroLinkedHashMap = new LinkedHashMap<>();
            // otroLinkedHashMap.put(4, "Cuatro");
            // otroLinkedHashMap.put(5, "Cinco");
            // linkedHashMap.putAll(otroLinkedHashMap);
            // System.out.println("LinkedHashMap después de copiar otro LinkedHashMap: " + linkedHashMap);

            // // 13. Reemplazar el valor asociado a una clave con un nuevo valor
            // linkedHashMap.replace(4, "NuevoCuatro");
            // System.out.println("LinkedHashMap después de reemplazar el valor asociado a '4': " + linkedHashMap);

            // // 14. Reemplazar el valor asociado a una clave solo si coincide con un valor específico
            // linkedHashMap.replace(4, "NuevoCuatro", "ReemplazadoCuatro");
            // System.out.println("LinkedHashMap después de reemplazar el valor asociado a '4' solo si es 'NuevoCuatro': " + linkedHashMap);

            // // 15. Reemplazar el valor asociado a una clave con el resultado de una función
            // linkedHashMap.replaceAll((k, v) -> v.toUpperCase());
            // System.out.println("LinkedHashMap después de reemplazar todos los valores con mayúsculas: " + linkedHashMap);

            // // 16. Clonar el LinkedHashMap
            // LinkedHashMap<Integer, String> cloneMap = (LinkedHashMap<Integer, String>) linkedHashMap.clone();
            // System.out.println("Clon del LinkedHashMap: " + cloneMap);

            // // 17. Verificar si dos LinkedHashMap son iguales
            // boolean sonIguales = linkedHashMap.equals(otroLinkedHashMap);
            // System.out.println("¿Son iguales los dos LinkedHashMaps?: " + sonIguales);

            // // 18. Calcular el hash del LinkedHashMap
            // int hash = linkedHashMap.hashCode();
            // System.out.println("Hash del LinkedHashMap: " + hash);

            // // 19. Obtener el valor asociado a una clave, o un valor predeterminado si la clave no está presente
            // String valorOrDefault = linkedHashMap.getOrDefault(6, "Seis");
            // System.out.println("Valor asociado a la clave '6' o predeterminado: " + valorOrDefault);

            // // 20. Insertar un mapeo solo si la clave no está presente en el LinkedHashMap
            // linkedHashMap.putIfAbsent(7, "Siete");
            // System.out.println("LinkedHashMap después de insertar '7' solo si la clave no está presente: " + linkedHashMap);

            // // 21. Obtener y eliminar el valor asociado a una clave si y solo si coincide con un valor específico
            // boolean eliminado = linkedHashMap.remove(7, "Siete");
            // System.out.println("¿Se eliminó la clave '7' con el valor 'Siete'?: " + eliminado);

            // // 22. Obtener y reemplazar el valor asociado a una clave con un nuevo valor
            // String valorReemplazado = linkedHashMap.replace(5, "ReemplazoCinco");
            // System.out.println("Valor reemplazado asociado a la clave '5': " + valorReemplazado);

            // // 23. Obtener y reemplazar el valor asociado a una clave con un nuevo valor solo si coincide con un valor específico
            // boolean reemplazado = linkedHashMap.replace(5, "ReemplazoCinco", "NuevoReemplazoCinco");
            // System.out.println("¿Se reemplazó el valor asociado a '5' solo si era 'ReemplazoCinco'?: " + reemplazado);

            // // 24. Obtener o calcular el valor asociado a una clave, y almacenarlo si no está presente en el LinkedHashMap
            // String valorComputado = linkedHashMap.computeIfAbsent(8, k -> "ComputadoOcho");
            // System.out.println("Valor computado asociado a la clave '8': " + valorComputado);

            // // 25. Calcular el valor asociado a una clave y reemplazar el valor existente si está presente en el LinkedHashMap
            // String valorCalculado = linkedHashMap.computeIfPresent(8, (k, v) -> v + " Modificado");
            // System.out.println("Valor calculado y reemplazado asociado a la clave '8': " + valorCalculado);

            // // 26. Calcular el valor asociado a una clave y almacenarlo en el LinkedHashMap
            // String valorCalculadoNuevo = linkedHashMap.compute(9, (k, v) -> "ComputadoNuevoNueve");
            // System.out.println("Valor calculado y almacenado asociado a la clave '9': " + valorCalculadoNuevo);

            // // 27. Fusionar el valor asociado a una clave con un nuevo valor si la clave está presente en el LinkedHashMap
            // linkedHashMap.merge(9, " Fusionado", (oldValue, newValue) -> oldValue.concat(newValue));
            // System.out.println("LinkedHashMap después de fusionar el valor asociado a '9': " + linkedHashMap);

            // // 28. Obtener una vista del submapa del LinkedHashMap
            // System.out.println("Submapa del LinkedHashMap: " + linkedHashMap.subMap(2, 5));

            // // 29. Obtener una vista del submapa del LinkedHashMap hasta una clave específica
            // System.out.println("Submapa del LinkedHashMap hasta '5': " + linkedHashMap.headMap(5));

            // // 30. Obtener una vista del submapa del LinkedHashMap desde una clave específica
            // System.out.println("Submapa del LinkedHashMap desde '5': " + linkedHashMap.tailMap(5));


            // TREESET - HASHSET - LINKEDHASHSET
            
            TreeSet<Integer> treeSet = new TreeSet<>();
            treeSet.add(3);
            treeSet.add(1);
            treeSet.add(2);
    
            System.out.println("Elementos en orden ascendente: " + treeSet);

            HashSet<Integer> hashSet = new HashSet<>();
            hashSet.add(3);
            hashSet.add(1);
            hashSet.add(2);
    
            System.out.println("Elementos en orden no específico: " + hashSet);

            LinkedHashSet<Integer> linkedHashSet = new LinkedHashSet<>();
            linkedHashSet.add(3);
            linkedHashSet.add(1);
            linkedHashSet.add(2);
    
            System.out.println("Elementos en orden de inserción: " + linkedHashSet);





            // 2. Obtener el primer elemento del TreeSet
            int primerElemento = treeSet.first();
            System.out.println("Primer elemento: " + primerElemento);

            // 3. Obtener el último elemento del TreeSet
            int ultimoElemento = treeSet.last();
            System.out.println("Último elemento: " + ultimoElemento);

            // 4. Obtener el elemento anterior a un elemento dado en el TreeSet
            int elementoAnterior = treeSet.lower(2);
            System.out.println("Elemento anterior a '2': " + elementoAnterior);

            // 5. Obtener el elemento posterior a un elemento dado en el TreeSet
            int elementoPosterior = treeSet.higher(2);
            System.out.println("Elemento posterior a '2': " + elementoPosterior);

            // 6. Eliminar el primer elemento del TreeSet y devolverlo
            int primerElementoEliminado = treeSet.pollFirst();
            System.out.println("Primer elemento eliminado: " + primerElementoEliminado);

            // 7. Eliminar el último elemento del TreeSet y devolverlo
            int ultimoElementoEliminado = treeSet.pollLast();
            System.out.println("Último elemento eliminado: " + ultimoElementoEliminado);

            // 8. Obtener el tamaño del TreeSet
            int tamano = treeSet.size();
            System.out.println("Tamaño del TreeSet: " + tamano);

            // 9. Comprobar si el TreeSet contiene un elemento específico
            boolean contieneElemento = treeSet.contains(2);
            System.out.println("¿Contiene '2'?: " + contieneElemento);

            // 10. Verificar si el TreeSet está vacío
            boolean estaVacio = treeSet.isEmpty();
            System.out.println("¿Está vacío?: " + estaVacio);

            // 11. Eliminar todos los elementos del TreeSet
            treeSet.clear();

            // 12. Copiar los elementos de otro TreeSet al TreeSet actual
            TreeSet<Integer> otroTreeSet = new TreeSet<>();
            otroTreeSet.add(4);
            otroTreeSet.add(5);
            treeSet.addAll(otroTreeSet);
            System.out.println("TreeSet después de copiar otro TreeSet: " + treeSet);

            // 13. Crear un subconjunto del TreeSet con elementos menores que un valor dado
            TreeSet<Integer> subSetMenorQue = (TreeSet<Integer>) treeSet.headSet(5);
            System.out.println("Subconjunto de elementos menores que '5': " + subSetMenorQue);

            // 14. Crear un subconjunto del TreeSet con elementos mayores que un valor dado
            TreeSet<Integer> subSetMayorQue = (TreeSet<Integer>) treeSet.tailSet(4);
            System.out.println("Subconjunto de elementos mayores que '4': " + subSetMayorQue);

            // 15. Crear un subconjunto del TreeSet con elementos en un rango específico
            TreeSet<Integer> subSetRango = (TreeSet<Integer>) treeSet.subSet(4, 6);
            System.out.println("Subconjunto de elementos en el rango [4, 6): " + subSetRango);

            // 16. Obtener una vista del conjunto de elementos del TreeSet
            System.out.println("Conjunto de elementos: " + treeSet);

            // 17. Obtener un iterador sobre los elementos del TreeSet
            System.out.print("Iterador sobre los elementos: ");
            for (Integer elemento : treeSet) {
                System.out.print(elemento + " ");
            }
            System.out.println();

            // 18. Clonar el TreeSet
            TreeSet<Integer> cloneSet = (TreeSet<Integer>) treeSet.clone();
            System.out.println("Clon del TreeSet: " + cloneSet);

            // 19. Obtener un subconjunto del TreeSet que comience desde un elemento dado
            TreeSet<Integer> subSetDesdeElemento = (TreeSet<Integer>) treeSet.tailSet(2, true);
            System.out.println("Subconjunto desde el elemento '2': " + subSetDesdeElemento);

            // 20. Obtener un subconjunto del TreeSet que termine en un elemento dado
            TreeSet<Integer> subSetHastaElemento = (TreeSet<Integer>) treeSet.headSet(4, true);
            System.out.println("Subconjunto hasta el elemento '4': " + subSetHastaElemento);

            // 21. Verificar si dos TreeSets son iguales
            boolean sonIguales = treeSet.equals(otroTreeSet);
            System.out.println("¿Son iguales los dos TreeSets?: " + sonIguales);

            // 22. Obtener el hashCode del TreeSet
            int hashCode = treeSet.hashCode();
            System.out.println("HashCode del TreeSet: " + hashCode);

            // 23. Obtener un subconjunto del TreeSet que contenga solo elementos mayores que un valor dado
            TreeSet<Integer> subSetMayorQueElemento = (TreeSet<Integer>) treeSet.tailSet(3);
            System.out.println("Subconjunto mayor que '3': " + subSetMayorQueElemento);

            // 24. Obtener un subconjunto del TreeSet que contenga solo elementos menores que un valor dado
            TreeSet<Integer> subSetMenorQueElemento = (TreeSet<Integer>) treeSet.headSet(3);
            System.out.println("Subconjunto menor que '3': " + subSetMenorQueElemento);

            // 25. Verificar si el TreeSet contiene todos los elementos de otro TreeSet
            boolean contieneTodos = treeSet.containsAll(otroTreeSet);
            System.out.println("¿Contiene todos los elementos de otro TreeSet?: " + contieneTodos);

            // 26. Eliminar todos los elementos de un TreeSet que no están en otro TreeSet
            treeSet.retainAll(otroTreeSet);
            System.out.println("TreeSet después de retener solo elementos presentes en otro TreeSet: " + treeSet);

            // 27. Eliminar todos los elementos de un TreeSet que están en otro TreeSet
            treeSet.removeAll(otroTreeSet);
            System.out.println("TreeSet después de eliminar elementos presentes en otro TreeSet: " + treeSet);

            // 28. Convertir el TreeSet en un arreglo
            Object[] arreglo = treeSet.toArray();
            System.out.println("Arreglo resultante: " + java.util.Arrays.toString(arreglo));

            // 29. Convertir el TreeSet en un arreglo tipado
            Integer[] arregloTipado = treeSet.toArray(new Integer[0]);
            System.out.println("Arreglo tipado resultante: " + java.util.Arrays.toString(arregloTipado));

            // 30. Convertir el TreeSet en una cadena de caracteres
            String cadena = treeSet.toString();
            System.out.println("Representación en cadena: " + cadena);




        }
}
