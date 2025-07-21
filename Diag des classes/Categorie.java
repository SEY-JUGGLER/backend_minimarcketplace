/***********************************************************************
 * Module:  Categorie.java
 * Author:  EL hadji Mor Seye
 * Purpose: Defines the Class Categorie
 ***********************************************************************/

import java.util.*;

/** @pdOid 68277ee2-b9fa-45cc-be86-a410ee8e327b */
public class Categorie {
   /** @pdOid a3094c0d-9334-43fe-9293-bd28f723d217 */
   public int idCategorie;
   /** @pdOid 2c5bce35-ded2-45c2-8251-ccaa1738b54c */
   public java.lang.String nomCategorie;
   
   /** @pdRoleInfo migr=no name=Anonce assc=appartient coll=java.util.Collection impl=java.util.HashSet mult=1..* side=A */
   public java.util.Collection<Anonce> anonce;
   
   
   /** @pdGenerated default getter */
   public java.util.Collection<Anonce> getAnonce() {
      if (anonce == null)
         anonce = new java.util.HashSet<Anonce>();
      return anonce;
   }
   
   /** @pdGenerated default iterator getter */
   public java.util.Iterator getIteratorAnonce() {
      if (anonce == null)
         anonce = new java.util.HashSet<Anonce>();
      return anonce.iterator();
   }
   
   /** @pdGenerated default setter
     * @param newAnonce */
   public void setAnonce(java.util.Collection<Anonce> newAnonce) {
      removeAllAnonce();
      for (java.util.Iterator iter = newAnonce.iterator(); iter.hasNext();)
         addAnonce((Anonce)iter.next());
   }
   
   /** @pdGenerated default add
     * @param newAnonce */
   public void addAnonce(Anonce newAnonce) {
      if (newAnonce == null)
         return;
      if (this.anonce == null)
         this.anonce = new java.util.HashSet<Anonce>();
      if (!this.anonce.contains(newAnonce))
         this.anonce.add(newAnonce);
   }
   
   /** @pdGenerated default remove
     * @param oldAnonce */
   public void removeAnonce(Anonce oldAnonce) {
      if (oldAnonce == null)
         return;
      if (this.anonce != null)
         if (this.anonce.contains(oldAnonce))
            this.anonce.remove(oldAnonce);
   }
   
   /** @pdGenerated default removeAll */
   public void removeAllAnonce() {
      if (anonce != null)
         anonce.clear();
   }

}