/***********************************************************************
 * Module:  Localisation.java
 * Author:  EL hadji Mor Seye
 * Purpose: Defines the Class Localisation
 ***********************************************************************/

import java.util.*;

/** @pdOid aab41716-f08d-4602-b39e-dc1af1ed369f */
public class Localisation {
   /** @pdOid 6936a7bb-9777-48e0-965a-c9308bb2da19 */
   public int idLocalisation;
   /** @pdOid 8a0c8a98-a8fc-414c-9f52-29820db1ee30 */
   public java.lang.String ville;
   /** @pdOid 6df5858e-3de9-4fa0-a9e8-56e6579fb938 */
   public java.lang.String quartier;
   
   /** @pdRoleInfo migr=no name=Anonce assc=localiser coll=java.util.Collection impl=java.util.HashSet mult=1..* side=A */
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