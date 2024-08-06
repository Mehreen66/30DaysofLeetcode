class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
      # 32-bit mask in hexadecimal
        mask = 0xFFFFFFFF
      # Works with both positive and negative integers
        while b != 0:
        # Compute carry, AND operation followed by left shift
          carry = (a & b) << 1
        # Sum without carry, XOR operation
          a = (a ^ b) & mask
        # Update b with the carry value
          b = carry & mask
    
    # Handle overflow for 32-bit signed integer
    # If a is negative, apply mask to get a 32-bit signed integer
        if a <= 0x7FFFFFFF:
          return a
        else:
          return ~(a ^ mask)
          
        