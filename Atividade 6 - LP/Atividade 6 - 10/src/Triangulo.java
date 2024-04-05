import javax.swing.*;

public class Triangulo {
    private float lado1;
    private float lado2;
    private float lado3;

    public void setLado1(float lado1) {
        this.lado1 = lado1;
    }

    public float getLado1() {
        return lado1;
    }

    public void setLado2(float lado2) {
        this.lado2 = lado2;
    }

    public float getLado2() {
        return lado2;
    }

    public void setLado3(float lado3) {
        this.lado3 = lado3;
    }

    public float getLado3() {
        return lado3;
    }

    // Implementação dos métodos
    float perimetro() {
        return lado1 + lado2 + lado3;
    }

    float area() {
        float semiPerimetro = perimetro() / 2;

        return (float) Math.sqrt(semiPerimetro * (semiPerimetro - lado1) * (semiPerimetro - lado2) * (semiPerimetro - lado3));
    }

    void verificarTriangulo() {
        if (lado1 == lado2 && lado1 == lado3) {
            JOptionPane.showMessageDialog(null,"O triangulo é equilátero");
        } else if (lado1 != lado2 && lado1 != lado3 && lado2 != lado3) {
            JOptionPane.showMessageDialog(null,"O triangulo é escaleno");
        } else {
            JOptionPane.showMessageDialog(null,"O triangulo é isósceles");
        }
    }
}
