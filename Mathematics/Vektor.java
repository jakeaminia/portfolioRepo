class Vektor {
  int dimensions;
  double[] components;
  double norm;

  Vektor() {
    dimensions = 3;
    components = new double[dimensions];
  }

  Vektor(int dimensions) {
    this.dimensions = dimensions;
    this.components = new double[dimensions];
  }

  double getComponent(int i) {
    return this.components[i - 1];
  }

  int getDimensions() {
    return dimensions;
  }

  double getNorm() {
    int compSum = 0;
    for (double val : components) {
      compSum += val * val;
    }
    return Math.sqrt(compSum);
  }

  String String() {
    String finalStr = "<";
    for (int i = 1; i <= this.getDimensions(); i++) {
      if (i == this.getDimensions()) {
        finalStr += this.getComponent(i) + ">";
      } else {
        finalStr += this.getComponent(i) + ", ";
      }
    }
    return finalStr;
  }

  void setComponent(int i, double val) {
    this.components[i - 1] = val;
  }

  Vektor scale(double scalar) {
    Vektor newVek = new Vektor(this.getDimensions());
    for (int i = 1; i <= this.getDimensions(); i++) {
      newVek.setComponent(i, this.getComponent(i) * scalar);
    }
    return newVek;
  }
}
