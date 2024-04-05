import javax.swing.*;

public class Main {

    public static void main(String[] args) {
        Triangulo triangulo = new Triangulo();

        // Atributos da classe Triângulo
        String valorDigitado = JOptionPane.showInputDialog("Digite o lado 1 do triângulo");
        float lado1 = Float.parseFloat(valorDigitado);
        triangulo.setLado1(lado1);

        valorDigitado = JOptionPane.showInputDialog("Digite o lado 2 do triângulo");
        float lado2 = Float.parseFloat(valorDigitado);
        triangulo.setLado2(lado2);

        valorDigitado = JOptionPane.showInputDialog("Digite o lado 3 do triângulo");
        float lado3 = Float.parseFloat(valorDigitado);
        triangulo.setLado3(lado3);

        // Métodos da classe Triângulo
        JOptionPane.showMessageDialog(null,"O lado 1 do triangulo é: " + triangulo.getLado1());
        JOptionPane.showMessageDialog(null,"O lado 2 do triangulo é: " + triangulo.getLado2());
        JOptionPane.showMessageDialog(null,"O lado 3 do triangulo é: " + triangulo.getLado3());

        JOptionPane.showMessageDialog(null,"O perímetro do triangulo é: " + triangulo.perimetro());
        JOptionPane.showMessageDialog(null,"A área do triangulo é: " + triangulo.area());
        triangulo.verificarTriangulo();


    }
    
}
