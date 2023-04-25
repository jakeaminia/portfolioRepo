import java.util.Arrays;
import java.util.Scanner;

class Matrix {
  private final int rows;
  private final int columns;
  private Double[][] grid;

  public static void main(String[] args) {

  }

  public Matrix(int rows, int columns) {
    this.rows = rows;
    this.columns = columns;
    this.grid = new Double[rows][columns];
  }

  public Matrix(Double[][] grid) {
    this.rows = grid.length;
    int row1len = grid[0].length;

    for (int i = 0; i < rows; i++) {
      if (grid[i].length != row1len) {
        throw new IllegalArgumentException();
      }
    }
    this.columns = row1len;
    this.grid = grid;
  }

  public int getRows() {
    return this.rows;
  }

  public int getColumns() {
    return this.columns;
  }

  public Double[][] getGrid() {
    return this.grid;
  }

  public Matrix transpose() {
    Double[][] result = new Double[this.columns][this.rows];
    for (int row = 0; row < this.rows; row++) {
      for (int column = 0; column < this.columns; column++) {
        result[column][row] = this.grid[row][column];
      }
    }
    return new Matrix(result);
  }

  public static Double dotProduct(Double[] vectorA, Double[] vectorB) {
    if (vectorA == null || vectorB == null || vectorA.length != vectorB.length) {
      return null;
    }
    double result = 0.0;
    for (int i = 0; i < vectorA.length; i++) {
      try {
        result += vectorA[i] * vectorB[i];
      } catch (NullPointerException e) {
        return null;
      }
    }
    return result;
  }

  public void setElement(int row, int column, double value) {
    if (row > 0 && row <= this.rows && column > 0 && column <= this.columns) {
      this.grid[row][column] = value;
    }
  }

  public Matrix matrixProduct(Matrix matrixB) {
    if (this.grid == null || matrixB.getGrid() == null || this.columns != matrixB.getRows()) {
      return null;
    }
    Matrix transposeB = matrixB.transpose();
    Double[][] result = new Double[this.rows][matrixB.getColumns()];
    for (int i = 0; i < this.rows; i++) {
      for (int j = 0; j < matrixB.getColumns(); j++) {
        result[i][j] = dotProduct(this.grid[i], transposeB.grid[j]);
      }
    }
    return new Matrix(result);
  }

  public Matrix squared() {
    return this.matrixProduct(this);
  }

  public Matrix gaussElimination() {
    Double[][] result = new Double[this.rows][this.columns];
    for (int i = 0; i < this.rows; i++) {
      System.arraycopy(this.grid[i], 0, result[i], 0, this.columns);
    }

    //For each row m:
    //a: find the first non-zero column n, pivot is grid[m][n]
    //b: locate first non-zero entry in column, swap it to pivot
    //c: operate on row to make element equal to 1
    //d: use pivot to clear non-zero entries in rows below it

    for (int currentRow = 0; currentRow < this.rows; currentRow++) {

      int firstNonZeroColumn = -1;
      int firstNonZeroEntry = -1;
      Double currentPivot = null;

      //a
      for (int column = 0; column < this.columns; column++) {
        for (int row = currentRow; row < this.rows; row++) {
          if (result[row][column] != 0) {
            firstNonZeroColumn = column;
            firstNonZeroEntry = row;
            currentPivot = result[row][column];
            break;
          }
        }
        if (firstNonZeroColumn != -1) {
          break;
        }
      }

      if (firstNonZeroColumn == -1) {
        return new Matrix(result);
      }

      if (firstNonZeroEntry != currentRow) {
        Double[] tempRow = result[firstNonZeroEntry];
        result[firstNonZeroEntry] = result[currentRow];
        result[currentRow] = tempRow;
      }

      for (int entryIndex = firstNonZeroColumn; entryIndex < columns; entryIndex++) {
        result[currentRow][entryIndex] /= currentPivot;
      }

      System.out.println("3" + Arrays.deepToString(result));

      for (int row = currentRow + 1; row < this.rows; row++) {
        Double constantToMultiply =
                result[row][firstNonZeroColumn] / result[currentRow][firstNonZeroColumn];

        System.out.println("4" + Arrays.deepToString(result));

        for (int entryIndex = 0; entryIndex < columns; entryIndex++) {
          result[row][entryIndex] -= constantToMultiply * result[currentRow][entryIndex];
        }

        System.out.println("5" + Arrays.deepToString(result));
      }

    }

    return new Matrix(result);
  }

  public String toString() {
    StringBuilder result = new StringBuilder();
    for (Double[] row : this.grid) {
      result.append(Arrays.toString(row)).append("\n");
    }
    return String.valueOf(result);
  }

}
