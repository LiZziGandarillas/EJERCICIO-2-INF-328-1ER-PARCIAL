using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary1 {
    public class Class1 {
        public Boolean esOperacion(string c) {
            string op = "+-*/";
            if (c != "" && op.Contains(c))
                return true;
            return false;
        }
        public int prioridad(string c) {
            string p = "+-";
            if (p.Contains(c))
                return 0;
            return 1;
        }
        public Boolean esNumero(string c) {
            string numero = "0123456789.";
            if (c != "" && numero.Contains(c))
                return true;
            return false;
        }

        public string operacion(string op, string num1, string num2) {
            double n1 = Double.Parse(num1.Replace(".", ","));
            double n2 = Double.Parse(num2.Replace(".", ","));
            if (op == "+") // suma
                return (n1 + n2).ToString().Replace(",", ".");
            if (op == "-") // resta
                return (n1 - n2).ToString().Replace(",", ".");
            if (op == "*") // multiplicaciob
                return (n1 * n2).ToString().Replace(",", ".");
            // division
            return (n1 / n2).ToString().Replace(",", ".");
        }

        public string Calcular(string expresion) {
            List<string> expr = new List<string>();
            foreach (char x in expresion)
                expr.Add(x + "");
            List<string> pilaChr = new List<string>();
            List<string> pilaNum = new List<string>();
            pilaNum.Add("0");
            string numero = "", num2, num1, c, d, top, op;
            while (expr.Count() > 0) {
                c = expr[0];
                expr.RemoveAt(0);
                if (expr.Count() > 0) {
                    d = expr[0];
                } else {
                    d = "";
                }
                if (esNumero(c)) {
                    numero += c;
                    if (!esNumero(d)) {
                        pilaNum.Add(numero);
                        numero = "";
                    }
                } else {
                    if (esOperacion(c)) {
                        while (true) {
                            if (pilaChr.Count() > 0) {
                                top = pilaChr[pilaChr.Count() - 1];
                            } else {
                                top = "";
                            }
                            if (esOperacion(top)) {
                                if (!(prioridad(c) > prioridad(top))) {
                                    num2 = pilaNum[pilaNum.Count() - 1];
                                    pilaNum.RemoveAt(pilaNum.Count() - 1);
                                    op = pilaChr[pilaChr.Count() - 1];
                                    pilaChr.RemoveAt(pilaChr.Count() - 1);
                                    num1 = pilaNum[pilaNum.Count() - 1];
                                    pilaNum.RemoveAt(pilaNum.Count() - 1);
                                    pilaNum.Add(operacion(op, num1, num2));
                                } else {
                                    pilaChr.Add(c);
                                    break;
                                }
                            } else {
                                pilaChr.Add(c);
                                break;
                            }
                        }
                    } else {
                        if (c == "(") {
                            pilaChr.Add(c);
                        } else {
                            if (c == ")") {
                                while (pilaChr.Count() > 0) {
                                    c = pilaChr[pilaChr.Count() - 1];
                                    pilaChr.RemoveAt(pilaChr.Count() - 1);
                                    if (c == "(") {
                                        break;
                                    } else {
                                        if (esOperacion(c)) {
                                            num2 = pilaNum[pilaNum.Count() - 1];
                                            pilaNum.RemoveAt(pilaNum.Count() - 1);
                                            num1 = pilaNum[pilaNum.Count() - 1];
                                            pilaNum.RemoveAt(pilaNum.Count() - 1);
                                            pilaNum.Add(operacion(c, num1, num2));
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            while (pilaChr.Count() > 0) {
                c = pilaChr[pilaChr.Count() - 1];
                pilaChr.RemoveAt(pilaChr.Count() - 1);
                if (c == "(")
                    break;
                else {
                    if (esOperacion(c)) {
                        num2 = pilaNum[pilaNum.Count() - 1];
                        pilaNum.RemoveAt(pilaNum.Count() - 1);
                        num1 = pilaNum[pilaNum.Count() - 1];
                        pilaNum.RemoveAt(pilaNum.Count() - 1);
                        pilaNum.Add(operacion(c, num1, num2));
                    }
                }
            }
            string respuesta = pilaNum[pilaNum.Count() - 1];
            pilaNum.RemoveAt(pilaNum.Count() - 1);
            return respuesta;
        }
    }
}
