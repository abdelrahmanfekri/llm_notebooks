### English Test Cases

1. **User Query:** ####I want to place an order. My name is John Doe, my phone number is 1234567890, and my address is 123 Main St.####
   **Expected Output:**

   ```json
   {
     "customer_phone_number": "1234567890",
     "customer_name": "John Doe",
     "customer_address": "123 Main St",
     "talk_to_human": false,
     "cancel_order": false,
     "confirm_order": false,
     "products_query": "",
     "business_query": ""
   }
   ```

2. **User Query:** ####Can I talk to a human?####
   **Expected Output:**

   ```json
   {
     "customer_phone_number": "",
     "customer_name": "",
     "customer_address": "",
     "talk_to_human": true,
     "cancel_order": false,
     "confirm_order": false,
     "products_query": "",
     "business_query": ""
   }
   ```

3. **User Query:** ####I want to cancel my order.####
   **Expected Output:**

   ```json
   {
     "customer_phone_number": "",
     "customer_name": "",
     "customer_address": "",
     "talk_to_human": false,
     "cancel_order": true,
     "confirm_order": false,
     "products_query": "",
     "business_query": ""
   }
   ```

4. **User Query:** ####Can you confirm my order?####
   **Expected Output:**

   ```json
   {
     "customer_phone_number": "",
     "customer_name": "",
     "customer_address": "",
     "talk_to_human": false,
     "cancel_order": false,
     "confirm_order": true,
     "products_query": "",
     "business_query": ""
   }
   ```

5. **User Query:** ####Do you have any laptops available?####
   **Expected Output:**

   ```json
   {
     "customer_phone_number": "",
     "customer_name": "",
     "customer_address": "",
     "talk_to_human": false,
     "cancel_order": false,
     "confirm_order": false,
     "products_query": "laptops",
     "business_query": ""
   }
   ```

6. **User Query:** ####What are your business hours?####
   **Expected Output:**

   ```json
   {
     "customer_phone_number": "",
     "customer_name": "",
     "customer_address": "",
     "talk_to_human": false,
     "cancel_order": false,
     "confirm_order": false,
     "products_query": "",
     "business_query": "business hours"
   }
   ```

7. **User Query:** ####I need to update my address to 456 Elm St.####
   **Expected Output:**

   ```json
   {
     "customer_phone_number": "",
     "customer_name": "",
     "customer_address": "456 Elm St",
     "talk_to_human": false,
     "cancel_order": false,
     "confirm_order": false,
     "products_query": "",
     "business_query": ""
   }
   ```

8. **User Query:** ####Can I get a refund?####
   **Expected Output:**

   ```json
   {
     "customer_phone_number": "",
     "customer_name": "",
     "customer_address": "",
     "talk_to_human": false,
     "cancel_order": false,
     "confirm_order": false,
     "products_query": "",
     "business_query": "refund"
   }
   ```

9. **User Query:** ####Do you sell smartphones?####
   **Expected Output:**

   ```json
   {
     "customer_phone_number": "",
     "customer_name": "",
     "customer_address": "",
     "talk_to_human": false,
     "cancel_order": false,
     "confirm_order": false,
     "products_query": "smartphones",
     "business_query": ""
   }
   ```

10. **User Query:** ####I want to place an order. My name is Jane Doe, my phone number is 0987654321, and my address is 789 Pine St.####
    **Expected Output:**

    ```json
    {
      "customer_phone_number": "0987654321",
      "customer_name": "Jane Doe",
      "customer_address": "789 Pine St",
      "talk_to_human": false,
      "cancel_order": false,
      "confirm_order": false,
      "products_query": "",
      "business_query": ""
    }
    ```

11. **User Query:** ####Can I speak to a representative?####
    **Expected Output:**

    ```json
    {
      "customer_phone_number": "",
      "customer_name": "",
      "customer_address": "",
      "talk_to_human": true,
      "cancel_order": false,
      "confirm_order": false,
      "products_query": "",
      "business_query": ""
    }
    ```

12. **User Query:** ####I need to cancel my order.####
    **Expected Output:**

    ```json
    {
      "customer_phone_number": "",
      "customer_name": "",
      "customer_address": "",
      "talk_to_human": false,
      "cancel_order": true,
      "confirm_order": false,
      "products_query": "",
      "business_query": ""
    }
    ```

13. **User Query:** ####Can you confirm my order for me?####
    **Expected Output:**

    ```json
    {
      "customer_phone_number": "",
      "customer_name": "",
      "customer_address": "",
      "talk_to_human": false,
      "cancel_order": false,
      "confirm_order": true,
      "products_query": "",
      "business_query": ""
    }
    ```

14. **User Query:** ####Do you have any tablets in stock?####
    **Expected Output:**

    ```json
    {
      "customer_phone_number": "",
      "customer_name": "",
      "customer_address": "",
      "talk_to_human": false,
      "cancel_order": false,
      "confirm_order": false,
      "products_query": "tablets",
      "business_query": ""
    }
    ```

15. **User Query:** ####What is your return policy?####
    **Expected Output:**
    ```json
    {
      "customer_phone_number": "",
      "customer_name": "",
      "customer_address": "",
      "talk_to_human": false,
      "cancel_order": false,
      "confirm_order": false,
      "products_query": "",
      "business_query": "return policy"
    }
    ```

### Arabic Test Cases

1.  **User Query:** ####أريد تقديم طلب. اسمي محمد علي، ورقم هاتفي هو 1234567890، وعنواني هو 123 شارع الرئيسي.####
    **Expected Output:**

    ```json
    {
      "customer_phone_number": "1234567890",
      "customer_name": "محمد علي",
      "customer_address": "123 شارع الرئيسي",
      "talk_to_human": false,
      "cancel_order": false,
      "confirm_order": false,
      "products_query": "",
      "business_query": ""
    }
    ```

2.  **User Query:** ####هل يمكنني التحدث إلى شخص؟####
    **Expected Output:**

    ```json
    {
      "customer_phone_number": "",
      "customer_name": "",
      "customer_address": "",
      "talk_to_human": true,
      "cancel_order": false,
      "confirm_order": false,
      "products_query": "",
      "business_query": ""
    }
    ```

3.  **User Query:** ####أريد إلغاء طلبي.####
    **Expected Output:**

    ```json
    {
      "customer_phone_number": "",
      "customer_name": "",
      "customer_address": "",
      "talk_to_human": false,
      "cancel_order": true,
      "confirm_order": false,
      "products_query": "",
      "business_query": ""
    }
    ```

4.  **User Query:** ####هل يمكنك تأكيد طلبي؟####
    **Expected Output:**

    ```json
    {
      "customer_phone_number": "",
      "customer_name": "",
      "customer_address": "",
      "talk_to_human": false,
      "cancel_order": false,
      "confirm_order": true,
      "products_query": "",
      "business_query": ""
    }
    ```

5.  **User Query:** ####هل لديكم أي أجهزة لابتوب متاحة؟####
    **Expected Output:**

    ```json
    {
      "customer_phone_number": "",
      "customer_name": "",
      "customer_address": "",
      "talk_to_human": false,
      "cancel_order": false,
      "confirm_order": false,
      "products_query": "أجهزة لابتوب",
      "business_query": ""
    }
    ```

6.  **User Query:** ####ما هي ساعات العمل لديكم؟####
    **Expected Output:**

    ```json
    {
      "customer_phone_number": "",
      "customer_name": "",
      "customer_address": "",
      "talk_to_human": false,
      "cancel_order": false,
      "confirm_order": false,
      "products_query": "",
      "business_query": "ساعات العمل"
    }
    ```

7.  **User Query:** ####أحتاج إلى تحديث عنواني إلى 456 شارع النخيل.####
    **Expected Output:**

    ```json
    {
      "customer_phone_number": "",
      "customer_name": "",
      "customer_address": "456 شارع النخيل",
      "talk_to_human": false,
      "cancel_order": false,
      "confirm_order": false,
      "products_query": "",
      "business_query": ""
    }
    ```

8.  **User Query:** ####هل يمكنني استرداد المبلغ؟####
    **Expected Output:**

    ```json
    {
      "customer_phone_number": "",
      "customer_name": "",
      "customer_address": "",
      "talk_to_human": false,
      "cancel_order": false,
      "confirm_order": false,
      "products_query": "",
      "business_query": "استرداد المبلغ"
    }
    ```

9.  **User Query:** ####هل تبيعون الهواتف الذكية؟####
    **Expected Output:**

    ```json
    {
      "customer_phone_number": "",
      "customer_name": "",
      "customer_address": "",
      "talk_to_human": false,
      "cancel_order": false,
      "confirm_order": false,
      "products_query": "الهواتف الذكية",
      "business_query": ""
    }
    ```

10. **User Query:** ####هل لديكم أي أجهزة تابلت في المخزون؟####
    **Expected Output:**

        ```json
        {
          "customer_phone_number": "",
          "customer_name": "",
          "customer_address": "",
          "talk_to_human": false,
          "cancel_order": false,
          "confirm_order": false,
          "products_query": "أجهزة تابلت",
          "business_query": ""
        }
        ```

    Sure, here are 15 test cases in Egyptian Arabic accent along with the expected output for each:

### Test Case 1

**User Query:** ####عايز أطلب أوردر####

**Expected Output:**

```json
{
  "customer_phone_number": "",
  "customer_name": "",
  "customer_address": "",
  "talk_to_human": false,
  "cancel_order": false,
  "confirm_order": false,
  "products_query": "",
  "business_query": ""
}
```

### Test Case 2

**User Query:** ####اسمي أحمد وعايز أطلب أوردر####

**Expected Output:**

```json
{
  "customer_phone_number": "",
  "customer_name": "أحمد",
  "customer_address": "",
  "talk_to_human": false,
  "cancel_order": false,
  "confirm_order": false,
  "products_query": "",
  "business_query": ""
}
```

### Test Case 3

**User Query:** ####رقمي 0123456789####

**Expected Output:**

```json
{
  "customer_phone_number": "0123456789",
  "customer_name": "",
  "customer_address": "",
  "talk_to_human": false,
  "cancel_order": false,
  "confirm_order": false,
  "products_query": "",
  "business_query": ""
}
```

### Test Case 4

**User Query:** ####عايز أكلم حد####

**Expected Output:**

```json
{
  "customer_phone_number": "",
  "customer_name": "",
  "customer_address": "",
  "talk_to_human": true,
  "cancel_order": false,
  "confirm_order": false,
  "products_query": "",
  "business_query": ""
}
```

### Test Case 5

**User Query:** ####عايز ألغي الأوردر####

**Expected Output:**

```json
{
  "customer_phone_number": "",
  "customer_name": "",
  "customer_address": "",
  "talk_to_human": false,
  "cancel_order": true,
  "confirm_order": false,
  "products_query": "",
  "business_query": ""
}
```

### Test Case 6

**User Query:** ####عايز أأكد الأوردر####

**Expected Output:**

```json
{
  "customer_phone_number": "",
  "customer_name": "",
  "customer_address": "",
  "talk_to_human": false,
  "cancel_order": false,
  "confirm_order": true,
  "products_query": "",
  "business_query": ""
}
```

### Test Case 7

**User Query:** ####فين الفرع بتاعكم####

**Expected Output:**

```json
{
  "customer_phone_number": "",
  "customer_name": "",
  "customer_address": "",
  "talk_to_human": false,
  "cancel_order": false,
  "confirm_order": false,
  "products_query": "",
  "business_query": "المكان"
}
```

### Test Case 8

**User Query:** ####عايز أعرف مواعيد العمل####

**Expected Output:**

```json
{
  "customer_phone_number": "",
  "customer_name": "",
  "customer_address": "",
  "talk_to_human": false,
  "cancel_order": false,
  "confirm_order": false,
  "products_query": "",
  "business_query": "مواعيد العمل"
}
```

### Test Case 9

**User Query:** ####فين منتجاتكم####

**Expected Output:**

```json
{
  "customer_phone_number": "",
  "customer_name": "",
  "customer_address": "",
  "talk_to_human": false,
  "cancel_order": false,
  "confirm_order": false,
  "products_query": "المنتجات",
  "business_query": ""
}
```

### Test Case 10

**User Query:** ####عايز أطلب بيتزا####

**Expected Output:**

```json
{
  "customer_phone_number": "",
  "customer_name": "",
  "customer_address": "",
  "talk_to_human": false,
  "cancel_order": false,
  "confirm_order": false,
  "products_query": "بيتزا",
  "business_query": ""
}
```

### Test Case 11

**User Query:** ####فين الفرع بتاعكم في المعادي####

**Expected Output:**

```json
{
  "customer_phone_number": "",
  "customer_name": "",
  "customer_address": "",
  "talk_to_human": false,
  "cancel_order": false,
  "confirm_order": false,
  "products_query": "",
  "business_query": "مكان الفرع المعادى"
}
```

### Test Case 13

**User Query:** ####عايز أطلب أوردر، اسمي علي، ورقمي 01098765432، وعنواني 123 شارع التحرير####

**Expected Output:**

```json
{
  "customer_phone_number": "01098765432",
  "customer_name": "علي",
  "customer_address": "123 شارع التحرير",
  "talk_to_human": false,
  "cancel_order": false,
  "confirm_order": false,
  "products_query": "",
  "business_query": ""
}
```

### Test Case 14

**User Query:** ####عايز أطلب أوردر، اسمي سارة####

**Expected Output:**

```json
{
  "customer_phone_number": "",
  "customer_name": "سارة",
  "customer_address": "",
  "talk_to_human": false,
  "cancel_order": false,
  "confirm_order": false,
  "products_query": "",
  "business_query": ""
}
```

### Test Case 15

**User Query:** ####عايز أطلب أوردر، اسمي كريم، ورقمي 0123456789، وعنواني 456 شارع النصر####

**Expected Output:**

```json
{
  "customer_phone_number": "0123456789",
  "customer_name": "كريم",
  "customer_address": "456 شارع النصر",
  "talk_to_human": false,
  "cancel_order": false,
  "confirm_order": false,
  "products_query": "",
  "business_query": ""
}
```
