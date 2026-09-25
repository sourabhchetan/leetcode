class Solution(object):
    def braceExpansionII(self, expression):
        n = len(expression)

        def parse(i):
            union = set()
            product = {""}

            while i < n and expression[i] != '}':
                if expression[i] == ',':
                    union |= product
                    product = {""}
                    i += 1

                elif expression[i] == '{':
                    part, i = parse(i + 1)

                    new_product = set()
                    for a in product:
                        for b in part:
                            new_product.add(a + b)

                    product = new_product

                else:
                    new_product = set()
                    for a in product:
                        new_product.add(a + expression[i])

                    product = new_product
                    i += 1

            union |= product

            if i < n and expression[i] == '}':
                i += 1

            return union, i

        result, _ = parse(0)
        return sorted(result)
