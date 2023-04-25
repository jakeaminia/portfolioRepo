import java.lang.Math;
import java.util.Locale;
import java.util.Scanner;
import jdk.internal.util.xml.impl.Input;

public class Vectors {

  public static void DisplayMenu() {
    System.out.print(
      "Hello! Welcome to the vector calculator! Which would you like to calculate?\n" +
      "a) Dot Product\n" +
      "b) Cross Product\n" +
      "c) Vector Length\n" +
      "d) Angle Between Vectors\n" +
      "e) Vector Projection\n" +
      "f) Scalar Projection\n" +
      "g) Distance Between Point and Plane\n" +
      "(MENU)\n" +
      "(EXIT)\n"
    );
  }

  public static double PointPlaneDist(double[] a, double[] b, double c) {
    double numerator = Math.abs(DotProduct(a, b) - c);
    double denominator = VectorLength(b);
    System.out.println(
      numerator +
      " / sqrt" +
      (Math.round(1000 * (denominator * denominator)) / 1000)
    );
    return numerator / denominator;
  }

  public static double AngleBetweenVectors(double[] a, double[] b) {
    double ADotB = Math.abs(DotProduct(a, b));
    System.out.println(
      "||a ⋅ b|| = " +
      ADotB +
      "\n||a|| = " +
      VectorLength(a) +
      "\n||b|| = " +
      VectorLength(b)
    );
    double sinTheta =
      Math.abs(DotProduct(a, b)) / (VectorLength(a) * VectorLength(b));
    double angle = Math.acos(sinTheta) * 180 / Math.PI;
    return angle;
  }

  public static double AngleBetweenVektors(Vektor a, Vektor b) {
    double ADotB = Math.abs(DotProdukt(a, b));
    System.out.println(
      "||a ⋅ b|| = " +
      ADotB +
      "\n||a|| = " +
      a.getNorm() +
      "\n||b|| = " +
      b.getNorm()
    );
    double sinTheta = Math.abs(DotProdukt(a, b)) / (a.getNorm() * b.getNorm());
    double angle = Math.acos(sinTheta) * 180 / Math.PI;
    return angle;
  }

  public static double ScalarProjection(double[] a, double[] b) {
    System.out.println(Math.abs(DotProduct(a, b)) + " / " + VectorLength(a));
    return (Math.abs(DotProduct(a, b)) / VectorLength(b));
  }

  public static double SkalarProjektion(Vektor a, Vektor b) {
    System.out.println(Math.abs(DotProdukt(a, b)) + " / " + a.getNorm());
    return (Math.abs(DotProdukt(a, b)) / b.getNorm());
  }

  public static double[] VectorProjection(double[] a, double[] b) {
    double scalar = DotProduct(a, b) / (VectorLength(b) * VectorLength(a));
    double[] result = { a[0] * scalar, a[1] * scalar, a[2] * scalar };
    return result;
  }

  public static Vektor VektorProjektion(Vektor a, Vektor b) {
    double scalar = DotProdukt(a, b) / (b.getNorm() * b.getNorm());
    Vektor result = a.scale(scalar);
    return result;
  }

  public static double VectorLength(double[] a) {
    double componentSum = 0;
    for (double val : a) {
      componentSum += val * val;
    }
    return (Math.sqrt(componentSum));
  }

  public static double[] CrossProduct(double[] a, double[] b) {
    double cx = a[1] * b[2] - a[2] * b[1];
    double cy = a[2] * b[0] - a[0] * b[2];
    double cz = a[0] * b[1] - a[1] * b[0];
    double[] result = { cx, cy, cz };
    return result;
  }

  public static Vektor KrossProdukt(Vektor a, Vektor b) {
    Vektor result = new Vektor();
    System.out.println(
      "" +
      a.getComponent(1) +
      a.getComponent(2) +
      a.getComponent(3) +
      b.getComponent(1) +
      b.getComponent(2) +
      b.getComponent(3)
    );
    if (a.getDimensions() == 3 && b.getDimensions() == 3) {
      double a1 = a.getComponent(1);
      double a2 = a.getComponent(2);
      double a3 = a.getComponent(3);
      double b1 = b.getComponent(1);
      double b2 = b.getComponent(2);
      double b3 = b.getComponent(3);
      double c1a = (a2 * b3);
      double c1b = (b2 * a3);
      double c1 = c1a - c1b;
      System.out.println("a2: " + a2 + " b3: " + b3 + " a2 * b3: " + (a2 * b3));
      double c2 = a3 * b1 - a1 * b3;
      double c3 = a1 * b2 - a2 * b1;
      result.setComponent(1,c1);
      result.setComponent(2,c2);
      result.setComponent(3,c3);
      System.out.println("Result: " + result.String());
    } else {
      System.out.println("Cross product can only be done with 3-D Vektors.");
    }

    return result;
  }

  public static double DotProduct(double[] a, double[] b) {
    double componentSum = 0;
    for (int i = 0; i < a.length; i++) {
      componentSum += a[i] * b[i];
    }
    return componentSum;
  }

  public static double DotProdukt(Vektor a, Vektor b) {
    double componentSum = 0;
    for (int i = 1; i <= a.getDimensions(); i++) {
      componentSum += a.getComponent(i) * b.getComponent(i);
    }
    return componentSum;
  }

  public static String VectorString(double[] vector) {
    String finalStr = "<";
    for (int i = 0; i < vector.length; i++) {
      if (i == vector.length - 1) {
        finalStr += vector[i] + ">";
      } else {
        finalStr += vector[i] + ", ";
      }
    }
    return finalStr;
  }

  public static double[] InputVector(char letter, int numDimensions) {
    Scanner scnr = new Scanner(System.in);
    if (numDimensions == 0) {
      System.out.println("How many dimensions are you working in?");
      numDimensions = scnr.nextInt();
    }
    System.out.println(
      "Enter the " + numDimensions + " components of vector " + letter + ": "
    );
    double[] vector = new double[numDimensions];

    for (int i = 0; i < numDimensions; i++) {
      vector[i] = scnr.nextDouble();
    }

    return vector;
  }

  public static double[] InputPlane(char letter) {
    Scanner scnr = new Scanner(System.in);
    System.out.println("How many dimensions are you working in?");
    int numDimensions = scnr.nextInt();
    System.out.println(
      "Enter the " + numDimensions + " coefficients of plane " + letter + ": "
    );
    double[] plane = new double[numDimensions];
    for (int i = 0; i < numDimensions; i++) {
      plane[i] = scnr.nextDouble();
    }
    return plane;
  }

  public static void main(String[] args) {
    Scanner scnr = new Scanner(System.in);
    boolean keepGoing = true;

    DisplayMenu();
    while (keepGoing == true) {
      switch (scnr.next().toLowerCase()) {
        case "a":
          System.out.println("You have chosen Dot Product.");
          double[] vectorA = InputVector('A', 0);
          double[] vectorB = InputVector('B', vectorA.length);
          double dotProduct = DotProduct(vectorA, vectorB);
          System.out.println(
            VectorString(vectorA) +
            " ⋅ " +
            VectorString(vectorB) +
            " = " +
            dotProduct
          );
          break;
        case "b":
          System.out.println("You have chosen Cross Product.");
          double[] vectorC = InputVector('A', 3);
          double[] vectorD = InputVector('B', 3);
          String crossProductString = VectorString(
            CrossProduct(vectorC, vectorD)
          );
          System.out.println(
            VectorString(vectorC) +
            " x " +
            VectorString(vectorD) +
            " = " +
            crossProductString
          );
          break;
        case "c":
          System.out.println("You have chosen Vector Length.");
          double[] vectorE = InputVector('A', 0);
          double vectorLength = VectorLength(vectorE);
          System.out.println("The length of the vector is: " + vectorLength);
          break;
        case "d":
          System.out.println("You have chosen Angle Between Vectors.");
          double[] vectorF = InputVector('A', 0);
          double[] vectorG = InputVector('B', vectorF.length);
          double vectorAngle = AngleBetweenVectors(vectorF, vectorG);
          System.out.println(
            "The angle between the two vectors is: " + vectorAngle
          );
          break;
        case "e":
          System.out.println("You have chosen Vector Projection.");
          double[] vectorH = InputVector('A', 0);
          double[] vectorI = InputVector('B', vectorH.length);
          System.out.println(
            "The Vector Projection of a onto b is: " +
            VectorString(VectorProjection(vectorH, vectorI))
          );
          break;
        case "f":
          System.out.println("You have chosen Scalar Projection.");
          double[] vectorJ = InputVector('A', 0);
          double[] vectorK = InputVector('B', vectorJ.length);
          System.out.println(
            "The Scalar Projection of a onto b is: " +
            ScalarProjection(vectorJ, vectorK)
          );
          break;
        case "g":
          System.out.println(
            "You have chose Distance Between Point and Plane."
          );
          double[] vectorL = InputVector('A', 0);
          double[] planeA = InputPlane('A');
          System.out.println(
            "Enter the value on the other side of the = for the plane."
          );
          double dValue = scnr.nextDouble();
          System.out.println(
            "The distance between the given point and plane is: " +
            PointPlaneDist(vectorL, planeA, dValue)
          );
          break;
        case "menu":
          DisplayMenu();
          break;
        case "exit":
          keepGoing = false;
          break;
        default:
          System.out.println(
            "Unfortunately, that option is not yet available."
          );
          break;
      }

      try {
        Thread.sleep(2000);
      } catch (InterruptedException e) {
        throw new RuntimeException("There seems to be a problem.\n");
      }
    }
  }
}
