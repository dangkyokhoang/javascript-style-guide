# <a name="airbnb-javascript-style-guide-">Định hướng Lối viết JavaScript của Airbnb() {</a>

*Một cách tiếp cận hợp lý đối với JavaScript*

> **Lưu ý của người dịch**: Bản dịch này, với nỗ lực truyền đạt nội dung bằng tiếng Việt nhiều nhất có thể, đã dịch sang tiếng Việt các thuật ngữ, và/hoặc các từ, cụm từ mà thông thường không được dịch, như: "style guide", "object", "polyfill", v.v. Nếu bạn cảm thấy không quen thuộc hoặc khó khăn trong việc hiểu một số từ trong bản dịch này, hoặc muốn biết các từ tương ứng trong Tiếng Anh, vui lòng tham khảo phần [Danh mục các Thuật ngữ](#terminology).

> **Lưu ý**: Định hướng này giả định bạn đang sử dụng [Babel](https://babeljs.io), và đòi hỏi bạn sử dụng [babel-preset-airbnb](https://npmjs.com/babel-preset-airbnb) hoặc một bộ tương đương. Nó cũng giả định rằng bạn đang cài bộ trợ năng cho ứng dụng của bạn, như [airbnb-browser-shims](https://npmjs.com/airbnb-browser-shims) hoặc một bộ tương đương.

[![Lượt tải](https://img.shields.io/npm/dm/eslint-config-airbnb.svg)](https://www.npmjs.com/package/eslint-config-airbnb)
[![Lượt tải](https://img.shields.io/npm/dm/eslint-config-airbnb-base.svg)](https://www.npmjs.com/package/eslint-config-airbnb-base)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/airbnb/javascript?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

Định hướng này cũng được dịch sang các ngôn ngữ khác. Xem phần [Dịch](#translation).

Các Định hướng Lối viết Khác

  - [ES5 (Đã lỗi thời)](https://github.com/airbnb/javascript/tree/es5-deprecated/es5)
  - [React](https://github.com/airbnb/javascript/blob/master/react)
  - [CSS-trong-JavaScript](https://github.com/airbnb/javascript/blob/master/css-in-javascript)
  - [CSS & Sass](https://github.com/airbnb/css)
  - [Ruby](https://github.com/airbnb/ruby)

## <a name="table-of-contents">Mục lục</a>

  1. [Các Kiểu giá trị](#types)
  1. [Các Tham chiếu](#references)
  1. [Các Đối tượng](#objects)
  1. [Các Mảng](#arrays)
  1. [Trích xuất](#destructuring)
  1. [Các Chuỗi](#strings)
  1. [Các Hàm](#functions)
  1. [Các Hàm mũi tên](#arrow-functions)
  1. [Các Lớp & các Hàm tạo](#classes--constructors)
  1. [Các Mô-đun](#modules)
  1. [Các Đối tượng duyệt and các Hàm sinh trị](#iterators-and-generators)
  1. [Các Thuộc tính](#properties)
  1. [Các Biến](#variables)
  1. [Sự kéo lên](#hoisting)
  1. [Các Toán tử So sánh và Sự bằng nhau](#comparison-operators--equality)
  1. [Các Khối](#blocks)
  1. [Các Câu lệnh Điều khiển](#control-statements)
  1. [Các Chú thích](#comments)
  1. [Khoảng trắng](#whitespace)
  1. [Các Dấu phẩy](#commas)
  1. [Các Dấu chấm phẩy](#semicolons)
  1. [Sự ép kiểu](#type-casting--coercion)
  1. [Các Quy ước Đặt tên](#naming-conventions)
  1. [Các Hàm truy cập](#accessors)
  1. [Các Sự kiện](#events)
  1. [jQuery](#jquery)
  1. [Tính tương thích của ECMAScript 5](#ecmascript-5-compatibility)
  1. [Lối viết ECMAScript 6+ (ES 2015+)](#ecmascript-6-es-2015-styles)
  1. [Thư viện Tiêu chuẩn](#standard-library)
  1. [Sự kiểm thử](#testing)
  1. [Hiệu suất](#performance)
  1. [Các Tài nguyên](#resources)
  1. [Thực tế Áp dụng](#in-the-wild)
  1. [Danh mục các Thuật ngữ](#terminology)
  1. [Dịch](#translation)
  1. [Về Hướng dẫn Lối viết JavaScript](#the-javascript-style-guide-guide)
  1. [Nói chuyện với Chúng tôi về JavaScript](#chat-with-us-about-javascript)
  1. [Những Người đóng góp](#contributors)
  1. [Giấy phép](#license)
  1. [Các Sửa đổi](#amendments)

## <a name="types">Các Kiểu giá trị</a>

  <a name="types--primitives"></a><a name="1.1"></a>
  - [1.1](#types--primitives) **Kiểu nguyên thủy**: Khi bạn truy cập một giá trị kiểu nguyên thủy, bạn làm việc trực tiếp trên giá trị của nó.

    - `string`
    - `number`
    - `boolean`
    - `null`
    - `undefined`
    - `symbol`

    ``` javascript
    const foo = 1;
    let bar = foo;

    bar = 9;

    console.log(foo, bar); // => 1, 9
    ```

    - Sự thiếu hỗ trợ cho các `Symbol` không thể được lấp đầy bởi các bộ trợ năng một cách toàn diện, do đó, chúng không nên được sử dụng khi hướng đến các trình duyệt/môi trường không có hỗ trợ sẵn.

  <a name="types--complex"></a><a name="1.2"></a>
  - [1.2](#types--complex) **Kiểu phức tạp**: Khi bạn truy cập một giá trị kiểu phức tạp, bạn làm việc trên tham chiếu giá trị của nó.

    - `object`
    - `array`
    - `function`

    ``` javascript
    const foo = [1, 2];
    const bar = foo;

    bar[0] = 9;

    console.log(foo[0], bar[0]); // => 9, 9
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="references">Các Tham chiếu</a>

  <a name="references--prefer-const"></a><a name="2.1"></a>
  - [2.1](#references--prefer-const) Sử dụng `const` đối với tất cả các tham chiếu; tránh sử dụng `var`. eslint: [`prefer-const`](https://eslint.org/docs/rules/prefer-const.html), [`no-const-assign`](https://eslint.org/docs/rules/no-const-assign.html)

    > Tại sao? Điều này đảm bảo rằng bạn không thể gán lại các tham chiếu, việc có thể gây ra các lỗi và gây khó khăn cho sự đọc hiểu mã nguồn.

    ``` javascript
    // không tốt
    var a = 1;
    var b = 2;

    // tốt
    const a = 1;
    const b = 2;
    ```

  <a name="references--disallow-var"></a><a name="2.2"></a>
  - [2.2](#references--disallow-var) Nếu bạn bắt buộc phải gán lại các tham chiếu, sử dụng `let`, thay vì `var`. eslint: [`no-var`](https://eslint.org/docs/rules/no-var.html)

    > Tại sao? `let` thuộc phạm vi khối mà nó được khởi tạo, thay vì thuộc phạm vi hàm như `var`.

    ``` javascript
    // không tốt
    var count = 1;
    if (true) {
      count += 1;
    }

    // tốt, sử dụng let.
    let count = 1;
    if (true) {
      count += 1;
    }
    ```

  <a name="references--block-scope"></a><a name="2.3"></a>
  - [2.3](#references--block-scope) Lưu ý rằng cả `let` và `const` đều thuộc phạm vi khối.

    ``` javascript
    // const và let chỉ tồn tại trong phạm vi khối tạo ra chúng.
    {
      let a = 1;
      const b = 1;
    }
    console.log(a); // ReferenceError
    console.log(b); // ReferenceError
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="objects">Các Đối tượng</a>

  <a name="objects--no-new"></a><a name="3.1"></a>
  - [3.1](#objects--no-new) Sử dụng cú pháp nguyên văn `{}` để khởi tạo đối tượng. eslint: [`no-new-object`](https://eslint.org/docs/rules/no-new-object.html)

    ``` javascript
    // không tốt
    const item = new Object();

    // tốt
    const item = {};
    ```

  <a name="es6-computed-properties"></a><a name="3.4"></a>
  - [3.2](#es6-computed-properties) Sử dụng các tên được tính của thuộc tính `[key()]` khi tạo các đối tượng có các tên của thuộc tính là động.

    > Tại sao? Chúng cho phép bạn định nghĩa tất cả các thuộc tính của một đối tượng cùng một chỗ.

    ``` javascript

    function getKey(k) {
      return `tên của thuộc tính là ${k}`;
    }

    // không tốt
    const obj = {
      id: 5,
      name: 'San Francisco',
    };
    obj[getKey('enabled')] = true;

    // tốt
    const obj = {
      id: 5,
      name: 'San Francisco',
      [getKey('enabled')]: true,
    };
    ```

  <a name="es6-object-shorthand"></a><a name="3.5"></a>
  - [3.3](#es6-object-shorthand) Sử dụng cú pháp định nghĩa phương thức rút gọn để định nghĩa các phương thức của đối tượng. eslint: [`object-shorthand`](https://eslint.org/docs/rules/object-shorthand.html)

    ``` javascript
    // không tốt
    const atom = {
      value: 1,

      addValue: function (value) {
        return atom.value + value;
      },
    };

    // tốt
    const atom = {
      value: 1,

      addValue(value) {
        return atom.value + value;
      },
    };
    ```

  <a name="es6-object-concise"></a><a name="3.6"></a>
  - [3.4](#es6-object-concise) Sử dụng cú pháp định nghĩa thuộc tính rút gọn để định nghĩa các thuộc tính của đối tượng. eslint: [`object-shorthand`](https://eslint.org/docs/rules/object-shorthand.html)

    > Tại sao? Nó ngắn gọn và súc tích.

    ``` javascript
    const lukeSkywalker = 'Luke Skywalker';

    // không tốt
    const obj = {
      lukeSkywalker: lukeSkywalker,
    };

    // tốt
    const obj = {
      lukeSkywalker,
    };
    ```

  <a name="objects--grouped-shorthand"></a><a name="3.7"></a>
  - [3.5](#objects--grouped-shorthand) Gom tất cả các thuộc tính rút gọn ở trên cùng khi khai báo đối tượng.

    > Tại sao? Điều này giúp bạn dễ dàng biết được thuộc tính nào sử dụng cú pháp rút gọn.

    ``` javascript
    const anakinSkywalker = 'Anakin Skywalker';
    const lukeSkywalker = 'Luke Skywalker';

    // không tốt
    const obj = {
      episodeOne: 1,
      twoJediWalkIntoACantina: 2,
      lukeSkywalker,
      episodeThree: 3,
      mayTheFourth: 4,
      anakinSkywalker,
    };

    // tốt
    const obj = {
      lukeSkywalker,
      anakinSkywalker,
      episodeOne: 1,
      twoJediWalkIntoACantina: 2,
      episodeThree: 3,
      mayTheFourth: 4,
    };
    ```

  <a name="objects--quoted-props"></a><a name="3.8"></a>
  - [3.6](#objects--quoted-props) Chỉ sử dụng dấu lược `' '` cho các thuộc tính có định danh không hợp lệ. eslint: [`quote-props`](https://eslint.org/docs/rules/quote-props.html)

    > Tại sao? Nhìn chung, chúng ta sẽ thấy nó dễ đọc hơn nhiều. Nó cải thiện nhấn mạnh cú pháp, và nó cũng giúp việc tối ưu hóa bằng các trình thực thi JS hiệu quả hơn.

    ``` javascript
    // không tốt
    const bad = {
      'foo': 3,
      'bar': 4,
      'một-cái-tên': 5,
    };

    // tốt
    const good = {
      foo: 3,
      bar: 4,
      'một-cái-tên': 5,
    };
    ```

  <a name="objects--prototype-builtins"></a>
  - [3.7](#objects--prototype-builtins) Không gọi các phương thức `Object.prototype` một cách trực tiếp, ví dụ như `hasOwnProperty`, `propertyIsEnumerable`, và `isPrototypeOf`. eslint: [`no-prototype-builtins`](https://eslint.org/docs/rules/no-prototype-builtins)

    > Tại sao? Những phương thức này có thể bị thay thế bởi các thuộc tính của một đối tượng - như `{ hasOwnProperty: false }` - hoặc, đối tượng có thể là một đối tượng rỗng (`Object.create(null)`).

    ``` javascript
    // không tốt
    console.log(object.hasOwnProperty(key));

    // tốt
    console.log(Object.prototype.hasOwnProperty.call(object, key));

    // tốt nhất
    const has = Object.prototype.hasOwnProperty; // lưu tạm phương thức một lần, dùng cho cả mô-đun.
    /* hoặc */
    import has from 'has'; // https://www.npmjs.com/package/has
    // ...
    console.log(has.call(object, key));
    ```

  <a name="objects--rest-spread"></a>
  - [3.8](#objects--rest-spread) Ưu tiên sử dụng toán tử liệt kê `...` so với [`Object.assign`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Object/assign) để tạo bản sao nhanh của một đối tượng. Sử dụng toán tử còn-lại `...` để tạo một đối tượng mới với một số thuộc tính đã bị loại bỏ
    ``` javascript
    // rất không tốt
    const original = { a: 1, b: 2 };
    const copy = Object.assign(original, { c: 3 }); // cái này làm biến đổi `original` ಠ_ಠ
    delete copy.a; // cái này cũng vậy

    // không tốt
    const original = { a: 1, b: 2 };
    const copy = Object.assign({}, original, { c: 3 }); // copy => { a: 1, b: 2, c: 3 }

    // tốt
    const original = { a: 1, b: 2 };
    const copy = { ...original, c: 3 }; // copy => { a: 1, b: 2, c: 3 }

    const { a, ...noA } = copy; // noA => { b: 2, c: 3 }
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="arrays">Các Mảng</a>

  <a name="arrays--literals"></a><a name="4.1"></a>
  - [4.1](#arrays--literals) Sử dụng cú pháp nguyên văn `[]` để khởi tạo mảng. eslint: [`no-array-constructor`](https://eslint.org/docs/rules/no-array-constructor.html)

    ``` javascript
    // không tốt
    const items = new Array();

    // tốt
    const items = [];
    ```

  <a name="arrays--push"></a><a name="4.2"></a>
  - [4.2](#arrays--push) Sử dụng [Array#push](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Array/push), thay vì phép gán, để thêm các mục cho một mảng.

    ``` javascript
    const someStack = [];

    // không tốt
    someStack[someStack.length] = 'abracadabra';

    // tốt
    someStack.push('abracadabra');
    ```

  <a name="es6-array-spreads"></a><a name="4.3"></a>
  - [4.3](#es6-array-spreads) Sử dụng toán tử liệt kê `...` để sao nhanh một mảng.

    ``` javascript
    // không tốt
    const len = items.length;
    const itemsCopy = [];
    let i;

    for (i = 0; i < len; i += 1) {
      itemsCopy[i] = items[i];
    }

    // tốt
    const itemsCopy = [...items];
    ```

  <a name="arrays--from"></a>
  <a name="arrays--from-iterable"></a><a name="4.4"></a>
  - [4.4](#arrays--from-iterable) Để chuyển đổi một đối tượng khả duyệt thành một mảng, sử dụng toán tử liệt kê `...` thay vì [`Array.from`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Array/from).

    ``` javascript
    const foo = document.querySelectorAll('.foo');

    // tốt
    const nodes = Array.from(foo);

    // tốt nhất
    const nodes = [...foo];
    ```

  <a name="arrays--from-array-like"></a>
  - [4.5](#arrays--from-array-like) Sử dụng [`Array.from`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Array/from) để chuyển đổi một đối tượng giống-mảng thành một mảng.

    ``` javascript
    const arrLike = { 0: 'foo', 1: 'bar', 2: 'baz', length: 3 };

    // không tốt
    const arr = Array.prototype.slice.call(arrLike);

    // tốt
    const arr = Array.from(arrLike);
    ```

  <a name="arrays--mapping"></a>
  - [4.6](#arrays--mapping) Sử dụng [`Array.from`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Array/from), thay vì toán tử liệt kê `...`, để ánh xạ một đối tượng khả duyệt, vì nó không tạo ra một mảng trung gian.

    ``` javascript
    // không tốt
    const baz = [...foo].map(bar);

    // tốt
    const baz = Array.from(foo, bar);
    ```

  <a name="arrays--callback-return"></a><a name="4.5"></a>
  - [4.7](#arrays--callback-return) Sử dụng các lệnh `return` cho các hàm gọi lại dùng cho các phương thức của mảng. Được phép bỏ qua `return` nếu phần thân hàm chỉ gồm một câu lệnh trả về một biểu thức không có hiệu ứng phụ, theo quy tắc [8.2](#arrows--implicit-return). eslint: [`array-callback-return`](https://eslint.org/docs/rules/array-callback-return)

    ``` javascript
    // tốt
    [1, 2, 3].map((x) => {
      const y = x + 1;
      return x * y;
    });

    // tốt
    [1, 2, 3].map(x => x + 1);

    // không tốt - không có giá trị trả về đồng nghĩa với `acc` sẽ trở thành undefined sau lượt duyệt đầu tiên
    [[0, 1], [2, 3], [4, 5]].reduce((acc, item, index) => {
      const flatten = acc.concat(item);
    });

    // tốt
    [[0, 1], [2, 3], [4, 5]].reduce((acc, item, index) => {
      const flatten = acc.concat(item);
      return flatten;
    });

    // không tốt
    inbox.filter((msg) => {
      const { subject, author } = msg;
      if (subject === 'Con chim nhại') {
        return author === 'Harper Lee';
      } else {
        return false;
      }
    });

    // tốt
    inbox.filter((msg) => {
      const { subject, author } = msg;
      if (subject === 'Con chim nhại') {
        return author === 'Harper Lee';
      }

      return false;
    });
    ```

  <a name="arrays--bracket-newline"></a>
  - [4.8](#arrays--bracket-newline) Sử dụng dấu ngắt dòng trước và sau các dấu đóng và mở ngoặc vuông nếu một mảng nằm trên nhiều dòng.

    ``` javascript
    // không tốt
    const arr = [
      [0, 1], [2, 3], [4, 5],
    ];

    const objectInArray = [{
      id: 1,
    }, {
      id: 2,
    }];

    const numberInArray = [
      1, 2,
    ];

    // tốt
    const arr = [[0, 1], [2, 3], [4, 5]];

    const objectInArray = [
      {
        id: 1,
      },
      {
        id: 2,
      },
    ];

    const numberInArray = [
      1,
      2,
    ];
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="destructuring">Trích xuất</a>

  <a name="destructuring--object"></a><a name="5.1"></a>
  - [5.1](#destructuring--object) Sử dụng trích xuất đối tượng khi truy cập và sử dụng nhiều thuộc tính của một đối tượng. eslint: [`prefer-destructuring`](https://eslint.org/docs/rules/prefer-destructuring)

    > Tại sao? Trích xuất giúp việc tạo các tham chiếu đến các thuộc tính trở nên dễ dàng hơn.

    ``` javascript
    // không tốt
    function getFullName(user) {
      const firstName = user.firstName;
      const lastName = user.lastName;

      return `${firstName} ${lastName}`;
    }

    // tốt
    function getFullName(user) {
      const { firstName, lastName } = user;
      return `${firstName} ${lastName}`;
    }

    // best
    function getFullName({ firstName, lastName }) {
      return `${firstName} ${lastName}`;
    }
    ```

  <a name="destructuring--array"></a><a name="5.2"></a>
  - [5.2](#destructuring--array) Hãy sử dụng trích xuất mảng. eslint: [`prefer-destructuring`](https://eslint.org/docs/rules/prefer-destructuring)

    ``` javascript
    const arr = [1, 2, 3, 4];

    // không tốt
    const first = arr[0];
    const second = arr[1];

    // tốt
    const [first, second] = arr;
    ```

  <a name="destructuring--object-over-array"></a><a name="5.3"></a>
  - [5.3](#destructuring--object-over-array) Sử dụng trích xuất đối tượng khi có nhiều giá trị trả về, thay vì trích xuất mảng.

    > Tại sao? Bạn có thể thêm các thuộc tính mới qua thời gian hay thay đổi thứ tự các thứ mà không lo làm hỏng các phép gọi trước đó.

    ``` javascript
    // không tốt
    function processInput(input) {
      // khi một phép màu xảy ra
      return [left, right, top, bottom];
    }

    // người gọi cần nghĩ về thứ tự của giá trị trả về
    const [left, __, top] = processInput(input);

    // tốt
    function processInput(input) {
      // khi một phép màu xảy ra
      return { left, right, top, bottom };
    }

    // người gọi chỉ cần chọn giá trị mà họ muốn
    const { left, top } = processInput(input);
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="strings">Các Chuỗi</a>

  <a name="strings--quotes"></a><a name="6.1"></a>
  - [6.1](#strings--quotes) Sử dụng dấu lược cho các chuỗi. eslint: [`quotes`](https://eslint.org/docs/rules/quotes.html)

    ``` javascript
    // không tốt
    const name = "Capt. Janeway";

    // không tốt - các nguyên văn mẫu nên chứa sự biến đổi chuỗi hoặc ngắt dòng
    const name = `Capt. Janeway`;

    // tốt
    const name = 'Capt. Janeway';
    ```

  <a name="strings--line-length"></a><a name="6.2"></a>
  - [6.2](#strings--line-length) Các chuỗi, dù khiến cho độ dài của dòng lớn hơn 100 ký tự, không nên được viết thành nhiều dòng sử dụng ghép chuỗi.

    > Tại sao? Các chuỗi bị chia nhỏ rất khó để làm việc cùng và khiến việc tìm kiếm trong mã nguồn trở nên khó hơn.

    ``` javascript
    // không tốt
    const errorMessage = 'Đây là một lỗi rất dài mà được ném ra bởi \
    Người Dơi. Khi bạn ngừng nghĩ về việc tại sao Người Dơi chẳng có liên \
    quan gì với thứ này, bạn sẽ vẫn chẳng đi đến đâu với \
    đâu.';

    // không tốt
    const errorMessage = 'Đây là một lỗi rất dài mà được ném ra bởi' +
        'Người Dơi. Khi bạn ngừng nghĩ về việc tại sao Người Dơi chẳng có liên' +
        'quan gì với thứ này, bạn sẽ vẫn chẳng đi đến đâu với' +
        'đâu.';

    // tốt
    const errorMessage = 'Đây là một lỗi rất dài mà được ném ra bởi Người Dơi. Khi bạn ngừng nghĩ về việc tại sao Người Dơi chẳng có liên quan gì với thứ này, bạn sẽ vẫn chẳng đi đến đâu với đâu.';
    ```

  <a name="es6-template-literals"></a><a name="6.4"></a>
  - [6.3](#es6-template-literals) Khi xây dựng các chuỗi theo một chu trình, sử dụng mẫu chuỗi thay vì ghép chuỗi. eslint: [`prefer-template`](https://eslint.org/docs/rules/prefer-template.html) [`template-curly-spacing`](https://eslint.org/docs/rules/template-curly-spacing)

    > Tại sao? Các mẫu chuỗi cho bạn một cú pháp súc tích, dễ đọc với các ngắt dòng và các tính năng ghép chuỗi phù hợp.

    ``` javascript
    // không tốt
    function sayHi(name) {
      return 'Bạn có khỏe không, ' + name + '?';
    }

    // không tốt
    function sayHi(name) {
      return ['Bạn có khỏe không, ', name, '?'].join();
    }

    // tốt
    function sayHi(name) {
      return `Bạn có khỏe không, ${name}?`;
    }
    ```

  <a name="strings--eval"></a><a name="6.5"></a>
  - [6.4](#strings--eval) Không bao giờ sử dụng `eval()` cho một chuỗi, điều đó mở ra rất nhiều các lỗ hổng và rủi ro. eslint: [`no-eval`](https://eslint.org/docs/rules/no-eval)

  <a name="strings--escaping"></a>
  - [6.5](#strings--escaping) Không sử dụng các ký tự thoát trong một chuỗi khi không cần thiết. eslint: [`no-useless-escape`](https://eslint.org/docs/rules/no-useless-escape)

    > Tại sao? Các dấu chéo ngược làm giảm tính khả đọc, vì thế chúng chỉ nên xuất hiện khi cần.

    ``` javascript
    // không tốt
    const foo = '\'cái này\' \đư\ợc \"cho trong ngoặc\"';

    // tốt
    const foo = '\'cái này\' được "cho trong ngoặc"';
    const foo = `tên của tôi là '${name}'`;
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="functions">Các Hàm</a>

  <a name="functions--declarations"></a><a name="7.1"></a>
  - [7.1](#functions--declarations) Sử dụng biểu thức hàm hữu danh thay vì khai báo hàm. eslint: [`func-style`](https://eslint.org/docs/rules/func-style)

    > Tại sao? Các khai báo hàm đều được kéo lên, đồng nghĩa với việc một hàm rất dễ có khả năng được sử dụng trước cả khi nó được định nghĩa trong tệp. Điều này làm giảm tính khả đọc và khả năng bảo trì. Nếu bạn thấy một hàm đủ lớn hoặc phức tạp đến mức ảnh hưởng đến việc đọc hiểu phần còn lại của tệp thì, có lẽ, nó nên được tách ra thành một mô-đun riêng! Đừng quên đặt tên cho biểu thức một cách rõ ràng, cho dù tên hàm có thể được suy ra từ tên biến chứa hàm đó (thường gặp ở các trình duyệt mới nhất hoặc các trình biên dịch như Babel). Điều này loại bỏ các nhận định liên quan đến ngăn xếp của một lỗi. ([Cuộc thảo luận](https://github.com/airbnb/javascript/issues/794))

    ``` javascript
    // không tốt
    function foo() {
      // ...
    }

    // không tốt
    const foo = function () {
      // ...
    };

    // tốt
    // tên riêng của hàm, phân biệt với tên tham chiếu được gọi khi cần sử dụng
    const short = function longUniqueMoreDescriptiveLexicalFoo() {
      // ...
    };
    ```

  <a name="functions--iife"></a><a name="7.2"></a>
  - [7.2](#functions--iife) Đặt các biểu thức hàm gọi tức thời trong ngoặc. eslint: [`wrap-iife`](https://eslint.org/docs/rules/wrap-iife.html)

    > Tại sao? Một biểu thức hàm gọi tức thời mà một đơn vị riêng - đặt nó và dấu ngoặc dùng để gọi nó `()` trong ngoặc để biểu đạt nó một cách rõ ràng. Cũng cần biết là, trong cái thế giới mà mô-đun ngập tràn mọi nơi như bây giờ, bạn cũng chả mấy khi cần dùng đến biểu thức hàm gọi tức thời.

    ``` javascript
    // biểu thức hàm gọi tức thời
    (function () {
      console.log('Xin chào đến với thế giới. Hãy đi theo tôi.');
    }());
    ```

  <a name="functions--in-blocks"></a><a name="7.3"></a>
  - [7.3](#functions--in-blocks) Không bao giờ khai báo một hàm bên trong một khối không phải hàm (`if`, `while`, v.v.). Thay vào đó, hãy gán hàm cho một biến. Các trình duyệt đều sẽ cho phép bạn làm điều đó, nhưng tiếc là, cách mà chúng diễn dịch là khác nhau. eslint: [`no-loop-func`](https://eslint.org/docs/rules/no-loop-func.html)

  <a name="functions--note-on-blocks"></a><a name="7.4"></a>
  - [7.4](#functions--note-on-blocks) **Ghi chú:** ECMA-262 định nghĩa một `khối` là tập hợp một hoặc một vài câu lệnh. Một khai báo hàm không phải là một câu lệnh.

    ``` javascript
    // không tốt
    if (currentUser) {
      function test() {
        console.log('Đừng!');
      }
    }

    // tốt
    let test;
    if (currentUser) {
      test = () => {
        console.log('Tốt đó.');
      };
    }
    ```

  <a name="functions--arguments-shadow"></a><a name="7.5"></a>
  - [7.5](#functions--arguments-shadow) Không bao giờ đặt tên một tham số là `arguments`. Tham số này sẽ được ưu tiên hơn đối tượng `arguments` được cung cấp cho mỗi phạm vi hàm.

    ``` javascript
    // không tốt
    function foo(name, options, arguments) {
      // ...
    }

    // tốt
    function foo(name, options, args) {
      // ...
    }
    ```

  <a name="es6-rest"></a><a name="7.6"></a>
  - [7.6](#es6-rest) Không bao giờ sử dụng `arguments`, thay vào đó, hãy sử dụng cú pháp còn-lại `...`. eslint: [`prefer-rest-params`](https://eslint.org/docs/rules/prefer-rest-params)

    > Tại sao? `...` định rõ các đối số mà bạn muốn lấy. Thêm nữa, kết quả của còn-lại là một mảng đúng nghĩa, thay vì chỉ là giống-mảng như `arguments`.

    ``` javascript
    // không tốt
    function concatenateAll() {
      const args = Array.prototype.slice.call(arguments);
      return args.join('');
    }

    // tốt
    function concatenateAll(...args) {
      return args.join('');
    }
    ```

  <a name="es6-default-parameters"></a><a name="7.7"></a>
  - [7.7](#es6-default-parameters) Sử dụng tham số mặc định thay vì làm biến đổi các đối số truyền vào hàm.

    ``` javascript
    // rất tệ
    function handleThings(opts) {
      // Không! Chúng ta không nên biến đổi các đối số.
      // Cái tệ thứ hai: Nếu opts là kiểu sai, nó sẽ bị đổi thành một đối tượng.
      // Đó có thể là điều bạn muốn, nhưng nó thi thoảng gây ra lỗi.
      opts = opts || {};
      // ...
    }

    // vẫn tệ
    function handleThings(opts) {
      if (opts === void 0) {
        opts = {};
      }
      // ...
    }

    // tốt
    function handleThings(opts = {}) {
      // ...
    }
    ```

  <a name="functions--default-side-effects"></a><a name="7.8"></a>
  - [7.8](#functions--default-side-effects) Tránh gây ra hiệu ứng phụ với tham số mặc định.

    > Tại sao? Chúng khá là rối để có thể hình dung.

    ``` javascript
    var b = 1;
    // không tốt
    function count(a = b++) {
      console.log(a);
    }
    count();  // 1
    count();  // 2
    count(3); // 3
    count();  // 3
    ```

  <a name="functions--defaults-last"></a><a name="7.9"></a>
  - [7.9](#functions--defaults-last) Luôn để các tham số mặc định ở sau cùng.

    ``` javascript
    // không tốt
    function handleThings(opts = {}, name) {
      // ...
    }

    // tốt
    function handleThings(name, opts = {}) {
      // ...
    }
    ```

  <a name="functions--constructor"></a><a name="7.10"></a>
  - [7.10](#functions--constructor) Không bao giờ sử dụng hàm tạo `Function` để tạo hàm. eslint: [`no-new-func`](https://eslint.org/docs/rules/no-new-func)

    > Tại sao? Tạo một hàm theo cách này cũng thực thi chuỗi giống như `eval()` vậy, thứ mà mở ra các lỗ hổng.

    ``` javascript
    // không tốt
    var add = new Function('a', 'b', 'return a + b');

    // vẫn là không tốt
    var subtract = Function('a', 'b', 'return a - b');
    ```

  <a name="functions--signature-spacing"></a><a name="7.11"></a>
  - [7.11](#functions--signature-spacing) Sử dụng các dấu cách giữa các bộ phận hàm. eslint: [`space-before-function-paren`](https://eslint.org/docs/rules/space-before-function-paren) [`space-before-blocks`](https://eslint.org/docs/rules/space-before-blocks)

    > Tại sao? Sự đồng nhất vẫn cứ là tốt, và bạn không cần phải thêm hoặc bớt dấu cách khi không đặt tên hàm.

    ``` javascript
    // không tốt
    const f = function(){};
    const g = function (){};
    const h = function() {};

    // tốt
    const x = function () {};
    const y = function a() {};
    ```

  <a name="functions--mutate-params"></a><a name="7.12"></a>
  - [7.12](#functions--mutate-params) Không bao giờ làm biến đổi các tham số. eslint: [`no-param-reassign`](https://eslint.org/docs/rules/no-param-reassign.html)

    > Tại sao? Việc can thiệp vào các đối tượng được truyền vào dưới dạng tham số có thể gây hiệu ứng phụ không mong muốn đối với biến tại tiến trình gọi.

    ``` javascript
    // không tốt
    function f1(obj) {
      obj.key = 1;
    }

    // tốt
    function f2(obj) {
      const key = Object.prototype.hasOwnProperty.call(obj, 'key') ? obj.key : 1;
    }
    ```

  <a name="functions--reassign-params"></a><a name="7.13"></a>
  - [7.13](#functions--reassign-params) Không bao giờ gán lại các tham số. eslint: [`no-param-reassign`](https://eslint.org/docs/rules/no-param-reassign.html)

    > Tại sao? Việc gán lại các tham số có thể dẫn tới hành vi không mong muốn, đặc biệt là khi truy cập đối tượng `arguments`. Nó cũng có thể gây ra một số vấn đề về tối ưu hóa, nhất là trong V8.

    ``` javascript
    // không tốt
    function f1(a) {
      a = 1;
      // ...
    }

    function f2(a) {
      if (!a) { a = 1; }
      // ...
    }

    // tốt
    function f3(a) {
      const b = a || 1;
      // ...
    }

    function f4(a = 1) {
      // ...
    }
    ```

  <a name="functions--spread-vs-apply"></a><a name="7.14"></a>
  - [7.14](#functions--spread-vs-apply) Ưu tiên sử dụng toán tử liệt kê `...` để gọi các hàm bất định. eslint: [`prefer-spread`](https://eslint.org/docs/rules/prefer-spread)

    > Tại sao? Nó nhìn sáng sủa hơn, bạn không cần phải đặt ngữ cảnh, và bạn cũng đâu thể dễ dàng kết hợp `new` với `apply`.

    ``` javascript
    // không tốt
    const x = [1, 2, 3, 4, 5];
    console.log.apply(console, x);

    // tốt
    const x = [1, 2, 3, 4, 5];
    console.log(...x);

    // không tốt
    new (Function.prototype.bind.apply(Date, [null, 2016, 8, 5]));

    // tốt
    new Date(...[2016, 8, 5]);
    ```

  <a name="functions--signature-invocation-indentation"></a>
  - [7.15](#functions--signature-invocation-indentation) Các hàm với các bộ phận hàm, hoặc các phép gọi, nằm trên nhiều dòng nên được căn đầu dòng như tất cả các danh sách nhiều dòng khác trong hướng dẫn này: với mỗi mục nằm trên một dòng riêng biệt, cùng với một dấu phẩy ngay sau mục cuối cùng. eslint: [`function-paren-newline`](https://eslint.org/docs/rules/function-paren-newline)

    ``` javascript
    // không tốt
    function foo(bar,
                 baz,
                 quux) {
      // ...
    }

    // tốt
    function foo(
      bar,
      baz,
      quux,
    ) {
      // ...
    }

    // không tốt
    console.log(foo,
      bar,
      baz);

    // tốt
    console.log(
      foo,
      bar,
      baz,
    );
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="arrow-functions">Các Hàm mũi tên</a>

  <a name="arrows--use-them"></a><a name="8.1"></a>
  - [8.1](#arrows--use-them) Khi bạn phải sử dụng một hàm vô danh (như khi cần truyền một hàm gọi lại trên cùng dòng), sử dụng ký pháp hàm mũi tên. eslint: [`prefer-arrow-callback`](https://eslint.org/docs/rules/prefer-arrow-callback.html), [`arrow-spacing`](https://eslint.org/docs/rules/arrow-spacing.html)

    > Tại sao? Nó tạo ra một hàm thực thi trên ngữ cảnh của `this`, thường là thứ bạn cần, và nó rất súc tích.

    > Khi nào thì không? Khi bạn có một hàm tương đối rắc rối, bạn cần phải chuyển lô-gíc của hàm đó sang biểu thức hàm hữu danh.

    ``` javascript
    // không tốt
    [1, 2, 3].map(function (x) {
      const y = x + 1;
      return x * y;
    });

    // tốt
    [1, 2, 3].map((x) => {
      const y = x + 1;
      return x * y;
    });
    ```

  <a name="arrows--implicit-return"></a><a name="8.2"></a>
  - [8.2](#arrows--implicit-return) Nếu như phần thân hàm chỉ gồm một câu lệnh trả về một [biểu thức](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators#Expressions) mà không có hiệu ứng phụ, bỏ qua dấu ngoặc nhọn và sử dụng trả về ngầm định. Nếu không, giữ nguyên dấu ngoặc và sử dụng lệnh `return`. eslint: [`arrow-parens`](https://eslint.org/docs/rules/arrow-parens.html), [`arrow-body-style`](https://eslint.org/docs/rules/arrow-body-style.html)

    > Tại sao? Cú pháp tiện lợi. Nó dễ đọc khi nhiều hàm nối chuỗi nhau.

    ``` javascript
    // không tốt
    [1, 2, 3].map(number => {
      const nextNumber = number + 1;
      `Một chuỗi có chứa số ${nextNumber}.`;
    });

    // tốt
    [1, 2, 3].map(number => `Một chuỗi có chứa số ${number + 1}.`);

    // tốt
    [1, 2, 3].map((number) => {
      const nextNumber = number + 1;
      return `Một chuỗi có chứa số ${nextNumber}.`;
    });

    // tốt
    [1, 2, 3].map((number, index) => ({
      [index]: number,
    }));

    // Không dùng trả về ngầm định khi có hiệu ứng phụ
    function foo(callback) {
      const val = callback();
      if (val === true) {
        // Thực hiện gì đó nếu hàm gọi lại trả về true
      }
    }

    let bool = false;

    // không tốt
    foo(() => bool = true);

    // tốt
    foo(() => {
      bool = true;
    });
    ```

  <a name="arrows--paren-wrap"></a><a name="8.3"></a>
  - [8.3](#arrows--paren-wrap) Trong trường hợp biểu thức nằm trên nhiều dòng, nhóm nó trong ngoặc để dễ đọc hơn.

    > Tại sao? Nó cho thấy một cách rõ ràng điểm bắt đầu và kết thúc hàm.

    ``` javascript
    // không tốt
    ['get', 'post', 'put'].map(httpMethod => Object.prototype.hasOwnProperty.call(
        httpMagicObjectWithAVeryLongName,
        httpMethod,
      )
    );

    // tốt
    ['get', 'post', 'put'].map(httpMethod => (
      Object.prototype.hasOwnProperty.call(
        httpMagicObjectWithAVeryLongName,
        httpMethod,
      )
    ));
    ```

  <a name="arrows--one-arg-parens"></a><a name="8.4"></a>
  - [8.4](#arrows--one-arg-parens) Nếu hàm của bạn nhận một đối số và không sử dụng ngoặc nhọn, loại bỏ dấu ngoặc tròn. Nếu không, luôn luôn thêm ngoặc tròn trước và sau các đối số cho rõ ràng và nhất quán. Ghi chú: việc luôn sử dụng dấu ngoặc tròn được chấp nhận, khi đó, sử dụng [tùy chọn “always”](https://eslint.org/docs/rules/arrow-parens#always) cho eslint. eslint: [`arrow-parens`](https://eslint.org/docs/rules/arrow-parens.html)

    > Tại sao? Nhìn bớt rối mắt.

    ``` javascript
    // không tốt
    [1, 2, 3].map((x) => x * x);

    // tốt
    [1, 2, 3].map(x => x * x);

    // tốt
    [1, 2, 3].map(number => (
      `Một chuỗi thật là dài với số ${number}. Nó quá dài để chúng ta có thể viết cùng dòng với dòng .map!`
    ));

    // không tốt
    [1, 2, 3].map(x => {
      const y = x + 1;
      return x * y;
    });

    // tốt
    [1, 2, 3].map((x) => {
      const y = x + 1;
      return x * y;
    });
    ```

  <a name="arrows--confusing"></a><a name="8.5"></a>
  - [8.5](#arrows--confusing) Tránh gây dễ nhầm lẫn giữa cú pháp hàm mũi tên (`=>`) với các toán tử so sánh (`<=`, `>=`). eslint: [`no-confusing-arrow`](https://eslint.org/docs/rules/no-confusing-arrow)

    ``` javascript
    // không tốt
    const itemHeight = item => item.height <= 256 ? item.largeSize : item.smallSize;

    // không tốt
    const itemHeight = (item) => item.height >= 256 ? item.largeSize : item.smallSize;

    // tốt
    const itemHeight = item => (item.height <= 256 ? item.largeSize : item.smallSize);

    // tốt
    const itemHeight = (item) => {
      const { height, largeSize, smallSize } = item;
      return height <= 256 ? largeSize : smallSize;
    };
    ```

  <a name="whitespace--implicit-arrow-linebreak"></a>
  - [8.6](#whitespace--implicit-arrow-linebreak) Cách đặt vị trí của phần thân hàm mũi tên với trả về ngầm định. eslint: [`implicit-arrow-linebreak`](https://eslint.org/docs/rules/implicit-arrow-linebreak)

    ``` javascript
    // không tốt
    foo =>
      bar;

    foo =>
      (bar);

    // tốt
    foo => bar;
    foo => (bar);
    foo => (
       bar
    )
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="classes--constructors">Các Lớp và các Hàm tạo</a>

  <a name="constructors--use-class"></a><a name="9.1"></a>
  - [9.1](#constructors--use-class) Luôn sử dụng `class`. Tránh việc can thiệp trực tiếp vào `prototype`.

    > Tại sao? Cú pháp `class` súc tích, dễ hiểu và dễ hình dung.

    ``` javascript
    // không tốt
    function Queue(contents = []) {
      this.queue = [...contents];
    }
    Queue.prototype.pop = function () {
      const value = this.queue[0];
      this.queue.splice(0, 1);
      return value;
    };

    // tốt
    class Queue {
      constructor(contents = []) {
        this.queue = [...contents];
      }
      pop() {
        const value = this.queue[0];
        this.queue.splice(0, 1);
        return value;
      }
    }
    ```

  <a name="constructors--extends"></a><a name="9.2"></a>
  - [9.2](#constructors--extends) Sử dụng `extends` cho thừa kế.

    > Tại sao? Nó là cách sẵn có để thừa kế nguyên mẫu mà không làm ảnh hưởng đến `instanceof`.

    ``` javascript
    // không tốt
    const inherits = require('inherits');
    function PeekableQueue(contents) {
      Queue.apply(this, contents);
    }
    inherits(PeekableQueue, Queue);
    PeekableQueue.prototype.peek = function () {
      return this.queue[0];
    };

    // tốt
    class PeekableQueue extends Queue {
      peek() {
        return this.queue[0];
      }
    }
    ```

  <a name="constructors--chaining"></a><a name="9.3"></a>
  - [9.3](#constructors--chaining) Các phương thức, mỗi khi có thể, hãy trả về `this` để tiện cho việc nối chuỗi phương thức.

    ``` javascript
    // không tốt
    Jedi.prototype.jump = function () {
      this.jumping = true;
      return true;
    };

    Jedi.prototype.setHeight = function (height) {
      this.height = height;
    };

    const luke = new Jedi();
    luke.jump(); // => true
    luke.setHeight(20); // => undefined

    // tốt
    class Jedi {
      jump() {
        this.jumping = true;
        return this;
      }

      setHeight(height) {
        this.height = height;
        return this;
      }
    }

    const luke = new Jedi();

    luke.jump()
      .setHeight(20);
    ```

  <a name="constructors--tostring"></a><a name="9.4"></a>
  - [9.4](#constructors--tostring) Có thể viết phương thức `toString()` tùy ý, chỉ cần đảm bản nó hoạt động hoàn hảo và không gây ra các hiệu ứng phụ.

    ``` javascript
    class Jedi {
      constructor(options = {}) {
        this.name = options.name || 'vô danh';
      }

      getName() {
        return this.name;
      }

      toString() {
        return `Jedi - ${this.getName()}`;
      }
    }
    ```

  <a name="constructors--no-useless"></a><a name="9.5"></a>
  - [9.5](#constructors--no-useless) Các lớp có một hàm tạo mặc định nếu không được chỉ định. Một hàm tạo rỗng, hoặc chỉ trỏ đến lớp cha, là không cần thiết. eslint: [`no-useless-constructor`](https://eslint.org/docs/rules/no-useless-constructor)

    ``` javascript
    // không tốt
    class Jedi {
      constructor() {}

      getName() {
        return this.name;
      }
    }

    // không tốt
    class Rey extends Jedi {
      constructor(...args) {
        super(...args);
      }
    }

    // tốt
    class Rey extends Jedi {
      constructor(...args) {
        super(...args);
        this.name = 'Rey';
      }
    }
    ```

  <a name="classes--no-duplicate-members"></a>
  - [9.6](#classes--no-duplicate-members) Tránh trùng lặp các thành viên của một lớp. eslint: [`no-dupe-class-members`](https://eslint.org/docs/rules/no-dupe-class-members)

    > Tại sao? Với các khai báo thành viên bị lặp, khai báo cuối được tự động ưu tiên - việc có sự trùng lặp gần như chắc chắn là một lỗi.

    ``` javascript
    // không tốt
    class Foo {
      bar() { return 1; }
      bar() { return 2; }
    }

    // tốt
    class Foo {
      bar() { return 1; }
    }

    // tốt
    class Foo {
      bar() { return 2; }
    }
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="modules">Các Mô-đun</a>

  <a name="modules--use-them"></a><a name="10.1"></a>
  - [10.1](#modules--use-them) Luôn sử dụng mô-đun (`import`/`export`) thay vì một hệ thống mô-đun phi chuẩn. Bạn luôn có thể dịch mã sang hệ thống mô-đun mà bạn thích.

    > Tại sao? Mô-đun là tương lai, hãy cùng sử dụng tương lai ngay lúc này.

    ``` javascript
    // không tốt
    const AirbnbStyleGuide = require('./AirbnbStyleGuide');
    module.exports = AirbnbStyleGuide.es6;

    // ok
    import AirbnbStyleGuide from './AirbnbStyleGuide';
    export default AirbnbStyleGuide.es6;

    // best
    import { es6 } from './AirbnbStyleGuide';
    export default es6;
    ```

  <a name="modules--no-wildcard"></a><a name="10.2"></a>
  - [10.2](#modules--no-wildcard) Không sử dụng ký tự đại diện để nhập.

    > Tại sao? Điều này đảm bảo bạn chỉ xuất mặc định một giá trị.

    ``` javascript
    // không tốt
    import * as AirbnbStyleGuide from './AirbnbStyleGuide';

    // tốt
    import AirbnbStyleGuide from './AirbnbStyleGuide';
    ```

  <a name="modules--no-export-from-import"></a><a name="10.3"></a>
  - [10.3](#modules--no-export-from-import) Và không xuất trực tiếp từ một lệnh nhập.

    > Tại sao? Mặc dù cấu trúc một dòng là súc tích, việc nhập một cách rõ ràng và xuất một cách rõ ràng làm cho mọi thứ nhất quán.

    ``` javascript
    // không tốt
    // tên tệp es6.js
    export { es6 as default } from './AirbnbStyleGuide';

    // tốt
    // tên tệp es6.js
    import { es6 } from './AirbnbStyleGuide';
    export default es6;
    ```

  <a name="modules--no-duplicate-imports"></a>
  - [10.4](#modules--no-duplicate-imports) Chỉ nhập từ một đường dẫn ở chung một chỗ.
 eslint: [`no-duplicate-imports`](https://eslint.org/docs/rules/no-duplicate-imports)
    > Tại sao? Có nhiều dòng nhập từ cùng một đường dẫn khiến mã nguồn trở nên khó bảo trì hơn.

    ``` javascript
    // không tốt
    import foo from 'foo';
    // … và nhập một vài thứ nữa … //
    import { named1, named2 } from 'foo';

    // tốt
    import foo, { named1, named2 } from 'foo';

    // tốt
    import foo, {
      named1,
      named2,
    } from 'foo';
    ```

  <a name="modules--no-mutable-exports"></a>
  - [10.5](#modules--no-mutable-exports) Không xuất các ràng buộc có thể bị biến đổi.
 eslint: [`import/no-mutable-exports`](https://github.com/benmosher/eslint-plugin-import/blob/master/docs/rules/no-mutable-exports.md)
    > Tại sao? Sự biến đổi, nói chung, nên được tránh, nhưng đặc biệt là đối với trường hợp xuất các giá trị có thể bị biến đổi. Trong khi kỹ thuật này có thể là cần thiết trong một số trường hợp đặc biệt, nhìn chung, chỉ nên xuất các giá trị là hằng.

    ``` javascript
    // không tốt
    let foo = 3;
    export { foo };

    // tốt
    const foo = 3;
    export { foo };
    ```

  <a name="modules--prefer-default-export"></a>
  - [10.6](#modules--prefer-default-export) Trong các mô-đun chỉ có một địa chỉ xuất, ưu tiên xuất mặc định thay vì xuất hữu danh.
 eslint: [`import/prefer-default-export`](https://github.com/benmosher/eslint-plugin-import/blob/master/docs/rules/prefer-default-export.md)
    > Tại sao? Nhằm khuyến khích các tệp chỉ xuất một giá trị, giúp mã nguồn dễ đọc và dễ bảo trì.

    ``` javascript
    // không tốt
    export function foo() {}

    // tốt
    export default function foo() {}
    ```

  <a name="modules--imports-first"></a>
  - [10.7](#modules--imports-first) Đặt tất cả các lệnh `import` trên cùng.
 eslint: [`import/first`](https://github.com/benmosher/eslint-plugin-import/blob/master/docs/rules/first.md)
    > Tại sao? Vì các lệnh `import` được kéo lên, việc đặt tất cả chúng ở trên cùng nhằm ngăn chặn các hành vi không đáng có.

    ``` javascript
    // không tốt
    import foo from 'foo';
    foo.init();

    import bar from 'bar';

    // tốt
    import foo from 'foo';
    import bar from 'bar';

    foo.init();
    ```

  <a name="modules--multiline-imports-over-newlines"></a>
  - [10.8](#modules--multiline-imports-over-newlines) Các lệnh nhập nhiều dòng nên được căn đầu dòng giống như các mảng hay đối tượng nguyên văn nhiều dòng.

    > Tại sao? Các đấu ngoặc nhọn đều có cùng các quy tắc căn đầu dòng như tất cả mọi khối ngoặc nhọn trong bản định hướng này, cùng với như dấu phẩy ở cuối.

    ``` javascript
    // không tốt
    import {longNameA, longNameB, longNameC, longNameD, longNameE} from 'path';

    // tốt
    import {
      longNameA,
      longNameB,
      longNameC,
      longNameD,
      longNameE,
    } from 'path';
    ```

  <a name="modules--no-webpack-loader-syntax"></a>
  - [10.9](#modules--no-webpack-loader-syntax) Không cho phép cú pháp bộ tải Webpack trong các lệnh nhập mô-đun.
 eslint: [`import/no-webpack-loader-syntax`](https://github.com/benmosher/eslint-plugin-import/blob/master/docs/rules/no-webpack-loader-syntax.md)
    > Tại sao? Vì sử dụng cú pháp Webpack trong các lệnh nhập gom mã thành một bộ tổng hợp mô-đun. Ưu tiên sử dụng cú pháp bộ tải trong `webpack.config.js`.

    ``` javascript
    // không tốt
    import fooSass from 'css!sass!foo.scss';
    import barCss from 'style!css!bar.css';

    // tốt
    import fooSass from 'foo.scss';
    import barCss from 'bar.css';
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="iterators-and-generators">Các Đối tượng duyệt và các Hàm sinh trị</a>

  <a name="iterators--nope"></a><a name="11.1"></a>
  - [11.1](#iterators--nope) Không sử dụng các đối tượng duyệt. Ưu tiên sử dụng các hàm bậc cao hơn của JavaScript thay vì các vòng lặp như `for-in` hay `for-of`. eslint: [`no-iterator`](https://eslint.org/docs/rules/no-iterator.html) [`no-restricted-syntax`](https://eslint.org/docs/rules/no-restricted-syntax)

    > Tại sao? Điều này đảm bảo việc thực hiện quy tắc bất biến. Làm việc với các hàm thuần mà trả về các giá trị sẽ dễ tưởng tượng hơn so với các hiệu ứng phụ.

    > Sử dụng `map()` / `every()` / `filter()` / `find()` / `findIndex()` / `reduce()` / `some()` / ... để duyệt qua một mảng, và `Object.keys()` / `Object.values()` / `Object.entries()` để tạo một mảng để bạn có thể duyệt qua một đối tượng.

    ``` javascript
    const numbers = [1, 2, 3, 4, 5];

    // không tốt
    let sum = 0;
    for (let num of numbers) {
      sum += num;
    }
    sum === 15;

    // tốt
    let sum = 0;
    numbers.forEach((num) => {
      sum += num;
    });
    sum === 15;

    // tốt nhất, sử dụng hàm
    const sum = numbers.reduce((total, num) => total + num, 0);
    sum === 15;

    // không tốt
    const increasedByOne = [];
    for (let i = 0; i < numbers.length; i++) {
      increasedByOne.push(numbers[i] + 1);
    }

    // tốt
    const increasedByOne = [];
    numbers.forEach((num) => {
      increasedByOne.push(num + 1);
    });

    // tốt nhất, vẫn là sử dụng hàm
    const increasedByOne = numbers.map(num => num + 1);
    ```

  <a name="generators--nope"></a><a name="11.2"></a>
  - [11.2](#generators--nope) Không sử dụng các hàm sinh trị `function*` vào thời điểm này.

    > Tại sao? Nó không thể được dịch mã sang ES5 một cách hoàn hảo.

  <a name="generators--spacing"></a>
  - [11.3](#generators--spacing) Nếu bạn bắt buộc phải dùng các hàm sinh trị, hoặc bạn bỏ qua [khuyến nghị của chúng tôi](#generators--nope), hãy đảm bảo rằng bạn sử dụng dấu cách giữa các bộ phận hàm một cách hợp lý. eslint: [`generator-star-spacing`](https://eslint.org/docs/rules/generator-star-spacing)

    > Tại sao? `function` và `*` là tạo thành một từ khóa riêng - `*` không phải là từ khóa điều chỉnh cho `function`, `function*` là một cấu tạo riêng biệt, khác với `function`.

    ``` javascript
    // không tốt
    function * foo() {
      // ...
    }

    // không tốt
    const bar = function * () {
      // ...
    };

    // không tốt
    const baz = function *() {
      // ...
    };

    // không tốt
    const quux = function*() {
      // ...
    };

    // không tốt
    function*foo() {
      // ...
    }

    // không tốt
    function *foo() {
      // ...
    }

    // rất tệ
    function
    *
    foo() {
      // ...
    }

    // rất rất tệ
    const wat = function
    *
    () {
      // ...
    };

    // tốt
    function* foo() {
      // ...
    }

    // tốt
    const foo = function* () {
      // ...
    };
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="properties">Các Thuộc tính</a>

  <a name="properties--dot"></a><a name="12.1"></a>
  - [12.1](#properties--dot) Sử dụng ký pháp chấm `.` để truy cập các thuộc tính. eslint: [`dot-notation`](https://eslint.org/docs/rules/dot-notation.html)

    ``` javascript
    const luke = {
      jedi: true,
      age: 28,
    };

    // không tốt
    const isJedi = luke['jedi'];

    // tốt
    const isJedi = luke.jedi;
    ```

  <a name="properties--bracket"></a><a name="12.2"></a>
  - [12.2](#properties--bracket) Sử dụng ký pháp ngoặc `[]` để truy cập thuộc tính với một biến.

    ``` javascript
    const luke = {
      jedi: true,
      age: 28,
    };

    function getProp(prop) {
      return luke[prop];
    }

    const isJedi = getProp('jedi');
    ```
  <a name="es2016-properties--exponentiation-operator"></a>
  - [12.3](#es2016-properties--exponentiation-operator) Sử dụng toán tử lũy thừa `**` để tính các lũy thừa. eslint: [`no-restricted-properties`](https://eslint.org/docs/rules/no-restricted-properties).

    ``` javascript
    // không tốt
    const binary = Math.pow(2, 10);

    // tốt
    const binary = 2 ** 10;
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="variables">Các Biến</a>

  <a name="variables--const"></a><a name="13.1"></a>
  - [13.1](#variables--const) Luôn sử dụng `const` hoặc `let` để khai báo biến. Không làm như vậy sẽ dẫn đến các biến toàn cục. Chúng ta muốn tránh việc làm ô nhiễm không gian tên toàn cục. Đội trưởng Hành tinh đã cảnh báo chúng ta. eslint: [`no-undef`](https://eslint.org/docs/rules/no-undef) [`prefer-const`](https://eslint.org/docs/rules/prefer-const)

    ``` javascript
    // không tốt
    superPower = new SuperPower();

    // tốt
    const superPower = new SuperPower();
    ```

  <a name="variables--one-const"></a><a name="13.2"></a>
  - [13.2](#variables--one-const) Sử dụng một `const` hoặc `let` khai báo cho mỗi biến hoặc phép gán. eslint: [`one-var`](https://eslint.org/docs/rules/one-var.html)

    > Tại sao? Khai báo theo cách này giúp dễ thêm các khai báo mới, và bạn chẳng phải nghĩ về việc phải dùng `;` hay `,`. Bạn còn có thể bước qua mỗi khai báo trong trình gỡ lỗi, thay vì nhảy qua toàn bộ chúng trong một bước.

    ``` javascript
    // không tốt
    const items = getItems(),
        goSportsTeam = true,
        dragonball = 'z';

    // không tốt
    // (so sánh với trên kia và thử tìm ra lỗi ở đây)
    const items = getItems(),
        goSportsTeam = true;
        dragonball = 'z';

    // tốt
    const items = getItems();
    const goSportsTeam = true;
    const dragonball = 'z';
    ```

  <a name="variables--const-let-group"></a><a name="13.3"></a>
  - [13.3](#variables--const-let-group) Nhóm tất cả các `const` và rồi nhóm tất cả các `let`.

    > Tại sao? Điều này hữu ích khi, sau đó, bạn sẽ cần gán lại một biến dựa trên các biến đã gán trước đó.

    ``` javascript
    // không tốt
    let i, len, dragonball,
        items = getItems(),
        goSportsTeam = true;

    // không tốt
    let i;
    const items = getItems();
    let dragonball;
    const goSportsTeam = true;
    let len;

    // tốt
    const goSportsTeam = true;
    const items = getItems();
    let dragonball;
    let i;
    let length;
    ```

  <a name="variables--define-where-used"></a><a name="13.4"></a>
  - [13.4](#variables--define-where-used) Chỉ gán biến khi cần, nhưng nhớ đặt chúng ở một nơi hợp lý.

    > Tại sao? `let` và `const` thuộc phạm vi khối, không phải phạm vi hàm.

    ``` javascript
    // không tốt - phép gọi hàm không cần thiết
    function checkName(hasName) {
      const name = getName();

      if (hasName === 'thí nghiệm') {
        return false;
      }

      if (name === 'thí nghiệm') {
        this.setName('');
        return false;
      }

      return name;
    }

    // tốt
    function checkName(hasName) {
      if (hasName === 'thí nghiệm') {
        return false;
      }

      const name = getName();

      if (name === 'thí nghiệm') {
        this.setName('');
        return false;
      }

      return name;
    }
    ```
  <a name="variables--no-chain-assignment"></a><a name="13.5"></a>
  - [13.5](#variables--no-chain-assignment) Đừng nối chuỗi các phép gán. eslint: [`no-multi-assign`](https://eslint.org/docs/rules/no-multi-assign)

    > Tại sao? Việc nối chuỗi các phép gán tạo ra các biến toàn cục ngầm định.

    ``` javascript
    // không tốt
    (function example() {
      // JavaScript diễn giải điều này như
      // let a = ( b = ( c = 1 ) );
      // Từ khóa let chỉ áp dụng đối với biến a; các biến b và c sẽ trở thành
      // các biến toàn cục.
      let a = b = c = 1;
    }());

    console.log(a); // ném ra ReferenceError
    console.log(b); // 1
    console.log(c); // 1

    // tốt
    (function example() {
      let a = 1;
      let b = a;
      let c = a;
    }());

    console.log(a); // ném ra ReferenceError
    console.log(b); // ném ra ReferenceError
    console.log(c); // ném ra ReferenceError

    // điều tương tự áp dụng với `const`
    ```

  <a name="variables--unary-increment-decrement"></a><a name="13.6"></a>
  - [13.6](#variables--unary-increment-decrement) Tránh việc sử dụng các phép tăng và giảm một ngôi (`++`, `--`). eslint [`no-plusplus`](https://eslint.org/docs/rules/no-plusplus)

    > Tại sao? Theo như tài liệu của eslint, các phép tăng hoặc giảm một ngôi phụ thuộc vào Quy tắc thêm dấu chấm phẩy tự động và có thể gây ra các lỗi câm trong việc tăng hoặc giảm các giá trị trong một ứng dụng. Sự diễn đạt cũng trở nên rõ ràng hơn khi bạn biến đổi các giá trị với các lệnh, như `num += 1`, thay vì `num++` hay `num ++`. Việc không cho phép các lệnh tăng hoặc giảm một ngôi cũng giúp bạn tránh được các sự tiền tăng/tiền giảm các giá trị một cách không chủ ý, điều có thể cũng gây ra những hành vi không mong muốn cho chương trình của bạn.

    ``` javascript
    // không tốt

    const array = [1, 2, 3];
    let num = 1;
    num++;
    --num;

    let sum = 0;
    let truthyCount = 0;
    for (let i = 0; i < array.length; i++) {
      let value = array[i];
      sum += value;
      if (value) {
        truthyCount++;
      }
    }

    // tốt

    const array = [1, 2, 3];
    let num = 1;
    num += 1;
    num -= 1;

    const sum = array.reduce((a, b) => a + b, 0);
    const truthyCount = array.filter(Boolean).length;
    ```

<a name="variables--linebreak"></a>
  - [13.7](#variables--linebreak) Tránh các dấu ngắt dòng trước và sau `=` trong một phép gán. Nếu phép gán của bạn vi phạm [`max-len`](https://eslint.org/docs/rules/max-len.html), hãy đặt giá trị trong ngoặc tròn. eslint [`operator-linebreak`](https://eslint.org/docs/rules/operator-linebreak.html).

    > Tại sao? Các dấu ngắt dòng quanh `=` có thể làm mờ nhạt giá trị trong phép gán.

    ``` javascript
    // không tốt
    const foo =
      superLongLongLongLongLongLongLongLongFunctionName();

    // không tốt
    const foo
      = 'một chuỗi rất rất rất rất rất rất rất rất rất rất là dài';

    // tốt
    const foo = (
      superLongLongLongLongLongLongLongLongFunctionName()
    );

    // tốt
    const foo = 'một chuỗi rất rất rất rất rất rất rất rất rất rất là dài';
    ```

<a name="variables--no-unused-vars"></a>
  - [13.8](#variables--no-unused-vars) Không cho phép các biến không được sử dụng. eslint: [`no-unused-vars`](https://eslint.org/docs/rules/no-unused-vars)

    > Tại sao? Các biến được khai báo nhưng không được sử dụng ở khắp mọi nơi trong mã gần như chắc chắn là một lỗi do sự cải tiến mã nguồn chưa hoàn thiện. Những biến như vậy chiếm chỗ trong mã và có thể gây ra sự khó hiểu cho người đọc.

    ``` javascript
    // không tốt

    var some_unused_var = 42;

    // Các biến chỉ-viết không được coi là đã được sử dụng.
    var y = 10;
    y = 5;

    // Một phép đọc để sửa chính nó không được coi là đã sử dụng.
    var z = 0;
    z = z + 1;

    // Đối số không được sử dụng.
    function getX(x, y) {
        return x;
    }

    // tốt

    function getXPlusY(x, y) {
      return x + y;
    }

    var x = 1;
    var y = a + 2;

    alert(getXPlusY(x, y));

    // 'type' được bỏ qua kể cả khi nó không được sử dụng vì còn có
    // các thuộc tính đồng đẳng còn-lại.
    // Đây là một cách để trích xuất một đối tượng mà bỏ qua một vài thuộc tính.
    var { type, ...coords } = data;
    // 'coords' bây giờ là 'data' đã loại bỏ thuộc tính 'type'.
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="hoisting">Sự kéo lên</a>

  <a name="hoisting--about"></a><a name="14.1"></a>
  - [14.1](#hoisting--about) Các khai báo bằng `var` được kéo lên đầu của phạm vi hàm gần nhất, còn phép gán thì không. Các khai báo bằng `const` và `let` thì mang trên mình một đặc tính khác là [Giai đoạn chết](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#Temporal_dead_zone). Điều này là quan trọng để biết tại sao [`typeof` không còn an toàn](http://es-discourse.com/t/why-typeof-is-no-longer-safe/15).

    ``` javascript
    // chúng ta biết thứ này sẽ không hoạt động (giả định rằng
    // không có biến toàn cục nào tên là notDefined)
    function example() {
      console.log(notDefined); // => ném ra ReferenceError
    }

    // việc khai báo một biến sau khi bạn
    // sử dụng biến đó vẫn sẽ chạy bởi vì
    // sự nổi lên của biến. Lưu ý: phép gán
    // giá trị `true` không được kéo lên.
    function example() {
      console.log(declaredButNotAssigned); // => undefined
      var declaredButNotAssigned = true;
    }

    // trình biên dịch sẽ kéo khai báo biến
    // lên trên đầu của phạm vi hàm,
    // điều này có nghĩa là ví dụ trên có thể được viết là:
    function example() {
      let declaredButNotAssigned;
      console.log(declaredButNotAssigned); // => undefined
      declaredButNotAssigned = true;
    }

    // dùng const và let
    function example() {
      console.log(declaredButNotAssigned); // => ném ra ReferenceError
      console.log(typeof declaredButNotAssigned); // => ném ra ReferenceError
      const declaredButNotAssigned = true;
    }
    ```

  <a name="hoisting--anon-expressions"></a><a name="14.2"></a>
  - [14.2](#hoisting--anon-expressions) Các biểu thức hàm vô danh sẽ được kéo tên biến lên, nhưng không được kéo phép gán hàm.

    ``` javascript
    function example() {
      console.log(anonymous); // => undefined

      anonymous(); // => TypeError anonymous is not a function

      var anonymous = function () {
        console.log('biểu thức hàm vô danh');
      };
    }
    ```

  <a name="hoisting--named-expresions"></a><a name="hoisting--named-expressions"></a><a name="14.3"></a>
  - [14.3](#hoisting--named-expressions) Biểu thức hàm hữu danh sẽ được kéo tên biến lên, nhưng không được kéo tên hàm và thân hàm.

    ``` javascript
    function example() {
      console.log(named); // => undefined

      named(); // => TypeError named is not a function

      superPower(); // => ReferenceError superPower is not defined

      var named = function superPower() {
        console.log('Nhìn tui đang bay nè');
      };
    }

    // điều tương tự cũng đúng nếu
    // tên hàm là trùng với tên biến.
    function example() {
      console.log(named); // => undefined

      named(); // => TypeError named is not a function

      var named = function named() {
        console.log('named');
      };
    }
    ```

  <a name="hoisting--declarations"></a><a name="14.4"></a>
  - [14.4](#hoisting--declarations) Khai báo hàm được kéo cả tên và thân hàm lên.

    ``` javascript
    function example() {
      superPower(); // => Nhìn tui đang bay nè

      function superPower() {
        console.log('Nhìn tui đang bay nè');
      }
    }
    ```

  - Để tìm hiểu thêm, tham khảo bài viết [JavaScript Scoping & Hoisting](http://www.adequatelygood.com/2010/2/JavaScript-Scoping-and-Hoisting/) bởi [Ben Cherry](http://www.adequatelygood.com/).

**[⬆ về đầu trang](#table-of-contents)**

## <a name="comparison-operators--equality">Các Toán tử So sánh và Sự bằng nhau</a>

  <a name="comparison--eqeqeq"></a><a name="15.1"></a>
  - [15.1](#comparison--eqeqeq) Sử dụng `===` và `!==` thay vì `==` và `!=`. eslint: [`eqeqeq`](https://eslint.org/docs/rules/eqeqeq.html)

  <a name="comparison--if"></a><a name="15.2"></a>
  - [15.2](#comparison--if) Các câu lệnh điều kiện như lệnh `if` xét biểu thức của chúng bằng cách ép kiểu bằng một phương thức ảo`ToBoolean` và đều tuân theo những quy tắc đơn giản sau:

    - **Các đối tượng** tương đương với **true**
    - **Undefined** tương đương với **false**
    - **Null** tương đương với **false**
    - **Các boolean** tương đương với **giá trị của boolean**
    - **Các số** tương đương với **false** nếu là **+0, -0, hoặc NaN**, còn không sẽ là **true**
    - **Các chuỗi** tương đương vớiv**false** nếu là một chuỗi rỗng `''`, còn không sẽ là **true**

    ``` javascript
    if ([0] && []) {
      // true
      // một mảng (dù là mảng rỗng) là một đối tượng,
      // mà đối tượng luôn tương đương với true
    }
    ```

  <a name="comparison--shortcuts"></a><a name="15.3"></a>
  - [15.3](#comparison--shortcuts) Sử dụng dạng rút gọn cho các boolean, nhưng dùng dạng so sánh cụ thể đối với chuỗi và số.

    ``` javascript
    // không tốt
    if (isValid === true) {
      // ...
    }

    // tốt
    if (isValid) {
      // ...
    }

    // không tốt
    if (name) {
      // ...
    }

    // tốt
    if (name !== '') {
      // ...
    }

    // không tốt
    if (collection.length) {
      // ...
    }

    // tốt
    if (collection.length > 0) {
      // ...
    }
    ```

  <a name="comparison--moreinfo"></a><a name="15.4"></a>
  - [15.4](#comparison--moreinfo) Để biết thêm chi tiết, xem bài viết [Truth Equality and JavaScript](https://javascriptweblog.wordpress.com/2011/02/07/truth-equality-and-javascript/#more-2108) bởi Angus Croll.

  <a name="comparison--switch-blocks"></a><a name="15.5"></a>
  - [15.5](#comparison--switch-blocks) Sử dụng các dấu ngoặc cho các khối của mệnh đề `case` và `default` nếu nó có chứa các khai báo (như `let`, `const`, `function`, và `class`). eslint: [`no-case-declarations`](https://eslint.org/docs/rules/no-case-declarations.html)

    > Tại sao? Các khai báo tồn tại trong cả khối `switch` nhưng chỉ được khởi tạo khi được gán, mà nó chỉ xảy ra khi `case` của nó xảy ra. Điều này gây ra các lỗi khi mà nhiều mệnh đề `case` muốn định nghĩa cùng một thứ.

    ``` javascript
    // không tốt
    switch (foo) {
      case 1:
        let x = 1;
        break;
      case 2:
        const y = 2;
        break;
      case 3:
        function f() {
          // ...
        }
        break;
      default:
        class C {}
    }

    // tốt
    switch (foo) {
      case 1: {
        let x = 1;
        break;
      }
      case 2: {
        const y = 2;
        break;
      }
      case 3: {
        function f() {
          // ...
        }
        break;
      }
      case 4:
        bar();
        break;
      default: {
        class C {}
      }
    }
    ```

  <a name="comparison--nested-ternaries"></a><a name="15.6"></a>
  - [15.6](#comparison--nested-ternaries) Các toán tử ba ngôi không nên được đặt trong ngoặc và thường được viết trên một dòng riêng. eslint: [`no-nested-ternary`](https://eslint.org/docs/rules/no-nested-ternary.html)

    ``` javascript
    // không tốt
    const foo = maybe1 > maybe2
      ? "hi hi"
      : value1 > value2 ? "hi hi" : null;

    // chia thành hai biểu thức ba ngôi riêng biệt
    // là tốt nhất
    const maybeNull = value1 > value2 ? 'hi hi' : null;
    const foo = maybe1 > maybe2 ? 'hi hi' : maybeNull;
    ```

  <a name="comparison--unneeded-ternary"></a><a name="15.7"></a>
  - [15.7](#comparison--unneeded-ternary) Tránh các câu lệnh ba ngôi không đáng có. eslint: [`no-unneeded-ternary`](https://eslint.org/docs/rules/no-unneeded-ternary.html)

    ``` javascript
    // không tốt
    const foo = a ? a : b;
    const bar = c ? true : false;
    const baz = c ? false : true;

    // tốt
    const foo = a || b;
    const bar = !!c;
    const baz = !c;
    ```

  <a name="comparison--no-mixed-operators"></a>
  - [15.8](#comparison--no-mixed-operators) Khi kết hợp các toán tử, nhớ đóng chúng trong ngoặc. Ngoại lệ duy nhất là các toán tử tiêu chuẩn (`+`, `-`, `*`, & `/`) vì chúng có thứ tự ưu tiên mà ai ai cũng hiểu. eslint: [`no-mixed-operators`](https://eslint.org/docs/rules/no-mixed-operators.html)

    > Tại sao? Điều này cả thiện tính khả đọc và làm rõ ý định của nhà phát triển.

    ``` javascript
    // không tốt
    const foo = a && b < 0 || c > 0 || d + 1 === 0;

    // không tốt
    const bar = a ** b - 5 % d;

    // không tốt
    // ai đó có thể bị rối và nghĩ nó là (a || b) && c
    if (a || b && c) {
      return d;
    }

    // tốt
    const foo = (a && b < 0) || c > 0 || (d + 1 === 0);

    // tốt
    const bar = (a ** b) - (5 % d);

    // tốt
    if (a || (b && c)) {
      return d;
    }

    // tốt
    const bar = a + b / c * d;
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="blocks">Các Khối</a>

  <a name="blocks--braces"></a><a name="16.1"></a>
  - [16.1](#blocks--braces) Sử dụng các dấu ngoặc cho các khối nhiều dòng. eslint: [`nonblock-statement-body-position`](https://eslint.org/docs/rules/nonblock-statement-body-position)

    ``` javascript
    // không tốt
    if (test)
      return false;

    // tốt
    if (test) return false;

    // tốt
    if (test) {
      return false;
    }

    // không tốt
    function foo() { return false; }

    // tốt
    function bar() {
      return false;
    }
    ```

  <a name="blocks--cuddled-elses"></a><a name="16.2"></a>
  - [16.2](#blocks--cuddled-elses) Nếu bạn đang sử dụng các khối nhiều dòng với `if` và `else`, đặt `else` trên cùng dòng với dấu đóng ngoặc của khối `if`. eslint: [`brace-style`](https://eslint.org/docs/rules/brace-style.html)

    ``` javascript
    // không tốt
    if (test) {
      thing1();
      thing2();
    }
    else {
      thing3();
    }

    // tốt
    if (test) {
      thing1();
      thing2();
    } else {
      thing3();
    }
    ```

  <a name="blocks--no-else-return"></a><a name="16.3"></a>
  - [16.3](#blocks--no-else-return) Nếu một khối `if` luôn thực hiện lệnh `return`, những khối `else` tiếp theo là không cần thiết. Một lệnh `return` trong một khối `else if` theo sau một khối `if` mà có chứa `return` có thể được tách thành nhiều khối `if`. eslint: [`no-else-return`](https://eslint.org/docs/rules/no-else-return)

    ``` javascript
    // không tốt
    function foo() {
      if (x) {
        return x;
      } else {
        return y;
      }
    }

    // không tốt
    function cats() {
      if (x) {
        return x;
      } else if (y) {
        return y;
      }
    }

    // không tốt
    function dogs() {
      if (x) {
        return x;
      } else {
        if (y) {
          return y;
        }
      }
    }

    // tốt
    function foo() {
      if (x) {
        return x;
      }

      return y;
    }

    // tốt
    function cats() {
      if (x) {
        return x;
      }

      if (y) {
        return y;
      }
    }

    // tốt
    function dogs(x) {
      if (x) {
        if (z) {
          return y;
        }
      } else {
        return z;
      }
    }
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="control-statements">Các Câu lệnh Điều khiển</a>

  <a name="control-statements"></a>
  - [17.1](#control-statements) Nếu trong trường hợp lệnh điều khiển (`if`, `while`, v.v.) của bạn trở lên quá dài và vượt quá giới hạn độ dài dòng, mỗi (nhóm) điều kiện có thể được đặt ở một dòng mới. Toán tử lô-gíc nên được đặt ở đầu dòng.

    > Tại sao? Việc đặt các toán tử ở đầu dòng giúp các toán tử được căn đều và tuân theo cùng một mô hình với việc nối chuỗi phương thức. Điều này cũng cải thiện tính khả đọc vì khiến cho việc theo dõi một lô-gíc phức tạp trở nên đơn giản hơn.

    ``` javascript
    // không tốt
    if ((foo === 123 || bar === 'abc') && doesItLookGoodWhenItBecomesThatLong() && isThisReallyHappening()) {
      thing1();
    }

    // không tốt
    if (foo === 123 &&
      bar === 'abc') {
      thing1();
    }

    // không tốt
    if (foo === 123
      && bar === 'abc') {
      thing1();
    }

    // không tốt
    if (
      foo === 123 &&
      bar === 'abc'
    ) {
      thing1();
    }

    // tốt
    if (
      foo === 123
      && bar === 'abc'
    ) {
      thing1();
    }

    // tốt
    if (
      (foo === 123 || bar === 'abc')
      && doesItLookGoodWhenItBecomesThatLong()
      && isThisReallyHappening()
    ) {
      thing1();
    }

    // tốt
    if (foo === 123 && bar === 'abc') {
      thing1();
    }
    ```

  <a name="control-statement--value-selection"></a><a name="control-statements--value-selection"></a>
  - [17.2](#control-statements--value-selection) Không sử dụng toán tử lựa chọn thay cho các câu lệnh điều khiển.

    ``` javascript
    // không tốt
    !isRunning && startRunning();

    // tốt
    if (!isRunning) {
      startRunning();
    }
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="comments">Các Chú thích</a>

  <a name="comments--multiline"></a><a name="17.1"></a>
  - [18.1](#comments--multiline) Sử dụng `/** ... */` cho các chú thích nhiều dòng.

    ``` javascript
    // không tốt
    // make() trả về một phần tử
    // dựa trên tag được truyền vào
    //
    // @param {String} tag
    // @return {Element} element
    function make(tag) {

      // ...

      return element;
    }

    // tốt
    /**
     * make() trả về một phần tử
     * dựa trên tag được truyền vào
     */
    function make(tag) {

      // ...

      return element;
    }
    ```

  <a name="comments--singleline"></a><a name="17.2"></a>
  - [18.2](#comments--singleline) Sử dụng `//` cho các chú thích một dòng. Đặt các chú thích một dòng ở một dòng riêng, bên trên chủ đề của chú thích. Để một dòng trống trước chú thích trừ khi chú thích là dòng đầu tiên của một khối.

    ``` javascript
    // không tốt
    const active = true;  // là thẻ hiện tại

    // tốt
    // là thẻ hiện tại
    const active = true;

    // không tốt
    function getType() {
      console.log('đang lấy loại...');
      // đặt loại mặc định là 'không phân loại'
      const type = this.type || 'không phân loại';

      return type;
    }

    // tốt
    function getType() {
      console.log('đang lấy loại...');

      // đặt loại mặc định là 'không phân loại'
      const type = this.type || 'không phân loại';

      return type;
    }

    // như này cũng tốt
    function getType() {
      // đặt loại mặc định là 'không phân loại'
      const type = this.type || 'không phân loại';

      return type;
    }
    ```

  <a name="comments--spaces"></a>
  - [18.3](#comments--spaces) Bắt đầu tất cả các chú thích bằng một dấu cách để dễ đọc hơn. eslint: [`spaced-comment`](https://eslint.org/docs/rules/spaced-comment)

    ``` javascript
    // không tốt
    //là thẻ hiện tại
    const active = true;

    // tốt
    // là thẻ hiện tại
    const active = true;

    // không tốt
    /**
     *make() trả về một phần tử
     *dựa trên tag được truyền vào
     */
    function make(tag) {

      // ...

      return element;
    }

    // tốt
    /**
     * make() trả về một phần tử
     * dựa trên tag được truyền vào
     */
    function make(tag) {

      // ...

      return element;
    }
    ```

  <a name="comments--actionitems"></a><a name="17.3"></a>
  - [18.4](#comments--actionitems) Thêm `FIXME` hoặc `TODO` vào đầu chú thích giúp các nhà phát triển dễ dàng biết được rằng bạn đang chỉ ra một vấn đề cần được xem lại, hoặc bạn đang đề xuất cách giải quyết cho vấn đề nên mà được áp dụng. Các hành động có thể như `FIXME: -- cần xem xét về thứ này` hoặc `TODO: -- cần áp dụng`.

  <a name="comments--fixme"></a><a name="17.4"></a>
  - [18.5](#comments--fixme) Sử dụng `// FIXME:` để chú giải các vấn đề.

    ``` javascript
    class Calculator extends Abacus {
      constructor() {
        super();

        // FIXME: không nên dùng biến toàn cục ở đây
        total = 0;
      }
    }
    ```

  <a name="comments--todo"></a><a name="17.5"></a>
  - [18.6](#comments--todo) Sử dụng `// TODO:` để chú giải các cách giải quyết cho các vấn đề.

    ``` javascript
    class Calculator extends Abacus {
      constructor() {
        super();

        // TODO: giá trị của total nên được chuyển thành tham số
        this.total = 0;
      }
    }
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="whitespace">Khoảng trắng</a>

  <a name="whitespace--spaces"></a><a name="18.1"></a>
  - [19.1](#whitespace--spaces) Sử dụng các tab ngắn (dấu cách) đặt về 2 dấu cách. eslint: [`indent`](https://eslint.org/docs/rules/indent.html)

    ``` javascript
    // không tốt
    function foo() {
    ∙∙∙∙let name;
    }

    // không tốt
    function bar() {
    ∙let name;
    }

    // tốt
    function baz() {
    ∙∙let name;
    }
    ```

  <a name="whitespace--before-blocks"></a><a name="18.2"></a>
  - [19.2](#whitespace--before-blocks) Đặt 1 cách trước dấu mở ngoặc. eslint: [`space-before-blocks`](https://eslint.org/docs/rules/space-before-blocks.html)

    ``` javascript
    // không tốt
    function test(){
      console.log('ví dụ');
    }

    // tốt
    function test() {
      console.log('ví dụ');
    }

    // không tốt
    dog.set('attr',{
      age: '1 năm',
      breed: 'Chó núi Bern',
    });

    // tốt
    dog.set('attr', {
      age: '1 năm',
      breed: 'Chó núi Bern',
    });
    ```

  <a name="whitespace--around-keywords"></a><a name="18.3"></a>
  - [19.3](#whitespace--around-keywords) Đặt 1 dấu cách trước dấu mở ngoặc tròn của các lệnh điều khiển (`if`, `while`, v.v.). Không đặt dấu cách giữa danh sách đối số và tên hàm trong các phép gọi và khai báo hàm. eslint: [`keyword-spacing`](https://eslint.org/docs/rules/keyword-spacing.html)

    ``` javascript
    // không tốt
    if(isJedi) {
      fight ();
    }

    // tốt
    if (isJedi) {
      fight();
    }

    // không tốt
    function fight () {
      console.log ('Uiiiiii!');
    }

    // tốt
    function fight() {
      console.log('Uiiiiii!');
    }
    ```

  <a name="whitespace--infix-ops"></a><a name="18.4"></a>
  - [19.4](#whitespace--infix-ops) Đặt dấu cách trước và sau các toán tử. eslint: [`space-infix-ops`](https://eslint.org/docs/rules/space-infix-ops.html)

    ``` javascript
    // không tốt
    const x=y+5;

    // tốt
    const x = y + 5;
    ```

  <a name="whitespace--newline-at-end"></a><a name="18.5"></a>
  - [19.5](#whitespace--newline-at-end) Kết thúc tệp với một dấu ngắt dòng. eslint: [`eol-last`](https://github.com/eslint/eslint/blob/master/docs/rules/eol-last.md)

    ``` javascript
    // không tốt
    import { es6 } from './AirbnbStyleGuide';
      // ...
    export default es6;
    ```

    ``` javascript
    // không tốt
    import { es6 } from './AirbnbStyleGuide';
      // ...
    export default es6;↵
    ↵
    ```

    ``` javascript
    // tốt
    import { es6 } from './AirbnbStyleGuide';
      // ...
    export default es6;↵
    ```

  <a name="whitespace--chains"></a><a name="18.6"></a>
  - [19.6](#whitespace--chains) Căn đầu dòng khi tạo các chuỗi phương thức (nhiều hơn 2 chuỗi phương thức). Đặt dấu chấm ở đầu, để nhấn mạnh dòng này là một phép gọi phương thức, không phải là một câu lệnh mới. eslint: [`newline-per-chained-call`](https://eslint.org/docs/rules/newline-per-chained-call) [`no-whitespace-before-property`](https://eslint.org/docs/rules/no-whitespace-before-property)

    ``` javascript
    // không tốt
    $('#items').find('.selected').highlight().end().find('.open').updateCount();

    // không tốt
    $('#items').
      find('.selected').
        highlight().
        end().
      find('.open').
        updateCount();

    // tốt
    $('#items')
      .find('.selected')
        .highlight()
        .end()
      .find('.open')
        .updateCount();

    // không tốt
    const leds = stage.selectAll('.led').data(data).enter().append('svg:svg').classed('led', true)
        .attr('width', (radius + margin) * 2).append('svg:g')
        .attr('transform', `translate(${radius + margin},${radius + margin})`)
        .call(tron.led);

    // tốt
    const leds = stage.selectAll('.led')
        .data(data)
      .enter().append('svg:svg')
        .classed('led', true)
        .attr('width', (radius + margin) * 2)
      .append('svg:g')
        .attr('transform', `translate(${radius + margin},${radius + margin})`)
        .call(tron.led);

    // tốt
    const leds = stage.selectAll('.led').data(data);
    ```

  <a name="whitespace--after-blocks"></a><a name="18.7"></a>
  - [19.7](#whitespace--after-blocks) Để một dòng trống sau mỗi khối và trước câu lệnh tiếp theo.

    ``` javascript
    // không tốt
    if (foo) {
      return bar;
    }
    return baz;

    // tốt
    if (foo) {
      return bar;
    }

    return baz;

    // không tốt
    const obj = {
      foo() {
      },
      bar() {
      },
    };
    return obj;

    // tốt
    const obj = {
      foo() {
      },

      bar() {
      },
    };

    return obj;

    // không tốt
    const arr = [
      function foo() {
      },
      function bar() {
      },
    ];
    return arr;

    // tốt
    const arr = [
      function foo() {
      },

      function bar() {
      },
    ];

    return arr;
    ```

  <a name="whitespace--padded-blocks"></a><a name="18.8"></a>
  - [19.8](#whitespace--padded-blocks) Không kê các khối với các dòng trống. eslint: [`padded-blocks`](https://eslint.org/docs/rules/padded-blocks.html)

    ``` javascript
    // không tốt
    function bar() {

      console.log(foo);

    }

    // không tốt
    if (baz) {

      console.log(qux);
    } else {
      console.log(foo);

    }

    // không tốt
    class Foo {

      constructor(bar) {
        this.bar = bar;
      }
    }

    // tốt
    function bar() {
      console.log(foo);
    }

    // tốt
    if (baz) {
      console.log(qux);
    } else {
      console.log(foo);
    }
    ```

  <a name="whitespace--no-multiple-blanks"></a>
  - [19.9](#whitespace--no-multiple-blanks) Do not use multiple blank lines to pad your code. eslint: [`no-multiple-empty-lines`](https://eslint.org/docs/rules/no-multiple-empty-lines)

    <!-- markdownlint-disable MD012 -->
    ``` javascript
    // không tốt
    class Person {
      constructor(fullName, email, birthday) {
        this.fullName = fullName;


        this.email = email;


        this.setAge(birthday);
      }


      setAge(birthday) {
        const today = new Date();


        const age = this.getAge(today, birthday);


        this.age = age;
      }


      getAge(today, birthday) {
        // ..
      }
    }

    // tốt
    class Person {
      constructor(fullName, email, birthday) {
        this.fullName = fullName;
        this.email = email;
        this.setAge(birthday);
      }

      setAge(birthday) {
        const today = new Date();
        const age = getAge(today, birthday);
        this.age = age;
      }

      getAge(today, birthday) {
        // ..
      }
    }
    ```

  <a name="whitespace--in-parens"></a><a name="18.9"></a>
  - [19.10](#whitespace--in-parens) Không thêm các dấu cách trong dấu ngoặc tròn. eslint: [`space-in-parens`](https://eslint.org/docs/rules/space-in-parens.html)

    ``` javascript
    // không tốt
    function bar( foo ) {
      return foo;
    }

    // tốt
    function bar(foo) {
      return foo;
    }

    // không tốt
    if ( foo ) {
      console.log(foo);
    }

    // tốt
    if (foo) {
      console.log(foo);
    }
    ```

  <a name="whitespace--in-brackets"></a><a name="18.10"></a>
  - [19.11](#whitespace--in-brackets) Không thêm các dấu cách trong các dấu ngoặc vuông. eslint: [`array-bracket-spacing`](https://eslint.org/docs/rules/array-bracket-spacing.html)

    ``` javascript
    // không tốt
    const foo = [ 1, 2, 3 ];
    console.log(foo[ 0 ]);

    // tốt
    const foo = [1, 2, 3];
    console.log(foo[0]);
    ```

  <a name="whitespace--in-braces"></a><a name="18.11"></a>
  - [19.12](#whitespace--in-braces) Thêm các dấu cách giữa các dấu ngoặc nhọn. eslint: [`object-curly-spacing`](https://eslint.org/docs/rules/object-curly-spacing.html)

    ``` javascript
    // không tốt
    const foo = {clark: 'kent'};

    // tốt
    const foo = { clark: 'kent' };
    ```

  <a name="whitespace--max-len"></a><a name="18.12"></a>
  - [19.13](#whitespace--max-len) Tránh các dòng mã có nhiều hơn 100 ký tự (kể cả khoảng trắng). Lưu ý: theo như [trên đây](#strings--line-length), các chuỗi được loại trừ bởi quy tắc này, và bạn không nên chia chúng ra. eslint: [`max-len`](https://eslint.org/docs/rules/max-len.html)

    > Tại sao? Điều này đảm bảo tính khả đọc và khả năng bảo trì.

    ``` javascript
    // không tốt
    const foo = jsonData && jsonData.foo && jsonData.foo.bar && jsonData.foo.bar.baz && jsonData.foo.bar.baz.quux && jsonData.foo.bar.baz.quux.xyzzy;

    // không tốt
    $.ajax({ method: 'POST', url: 'https://airbnb.com/', data: { name: 'John' } }).done(() => console.log('Chúc mừng!')).fail(() => console.log('You have failed this city.'));

    // tốt
    const foo = jsonData
      && jsonData.foo
      && jsonData.foo.bar
      && jsonData.foo.bar.baz
      && jsonData.foo.bar.baz.quux
      && jsonData.foo.bar.baz.quux.xyzzy;

    // tốt
    $.ajax({
      method: 'POST',
      url: 'https://airbnb.com/',
      data: { name: 'John' },
    })
      .done(() => console.log('Chúc mừng!'))
      .fail(() => console.log('You have failed this city.'));
    ```

  <a name="whitespace--block-spacing"></a>
  - [19.14](#whitespace--block-spacing) Đảm bảo sự nhất quán về dấu cách sau dấu mở ngoặc và trước ký tự đầu tiên sau nó trên cùng một dòng. Quy tắc này cũng yêu cầu sự nhất quán về dấu cách trước dấu đóng ngoặc và sau ký tự cuối cùng trước nó trên cùng một dòng. eslint: [`block-spacing`](https://eslint.org/docs/rules/block-spacing)

    ``` javascript
    // không tốt
    function foo() {return true;}
    if (foo) { bar = 0;}

    // tốt
    function foo() { return true; }
    if (foo) { bar = 0; }
    ```

  <a name="whitespace--comma-spacing"></a>
  - [19.15](#whitespace--comma-spacing) Không sử dụng dấu cách trước dấu phẩy và phải sử dụng dấu cách sau dấu phẩy. eslint: [`comma-spacing`](https://eslint.org/docs/rules/comma-spacing)

    ``` javascript
    // không tốt
    var foo = 1,bar = 2;
    var arr = [1 , 2];

    // tốt
    var foo = 1, bar = 2;
    var arr = [1, 2];
    ```

  <a name="whitespace--computed-property-spacing"></a>
  - [19.16](#whitespace--computed-property-spacing) Không đặt dấu cách bên trong dấu ngoặc của thuộc tính được tính. eslint: [`computed-property-spacing`](https://eslint.org/docs/rules/computed-property-spacing)

    ``` javascript
    // không tốt
    obj[foo ]
    obj[ 'foo']
    var x = {[ b ]: a}
    obj[foo[ bar ]]

    // tốt
    obj[foo]
    obj['foo']
    var x = { [b]: a }
    obj[foo[bar]]
    ```

  <a name="whitespace--func-call-spacing"></a>
  - [19.17](#whitespace--func-call-spacing) Tránh sử dụng dấu cách giữa các hàm và phép gọi chúng. eslint: [`func-call-spacing`](https://eslint.org/docs/rules/func-call-spacing)

    ``` javascript
    // không tốt
    func ();

    func
    ();

    // tốt
    func();
    ```

  <a name="whitespace--key-spacing"></a>
  - [19.18](#whitespace--key-spacing) Đặt dấu cách giữa các tên và giá trị của các thuộc tính nguyên văn. eslint: [`key-spacing`](https://eslint.org/docs/rules/key-spacing)

    ``` javascript
    // không tốt
    var obj = { "foo" : 42 };
    var obj2 = { "foo":42 };

    // tốt
    var obj = { "foo": 42 };
    ```

  <a name="whitespace--no-trailing-spaces"></a>
  - [19.19](#whitespace--no-trailing-spaces) Tránh các dấu cách ở cuối các dòng. eslint: [`no-trailing-spaces`](https://eslint.org/docs/rules/no-trailing-spaces)

  <a name="whitespace--no-multiple-empty-lines"></a>
  - [19.20](#whitespace--no-multiple-empty-lines) Tránh để nhiều dòng trống liên tiếp và chỉ cho một dòng trống ở cuối tệp. eslint: [`no-multiple-empty-lines`](https://eslint.org/docs/rules/no-multiple-empty-lines)

    <!-- markdownlint-disable MD012 -->
    ``` javascript
    // không tốt
    var x = 1;



    var y = 2;

    // tốt
    var x = 1;

    var y = 2;
    ```
    <!-- markdownlint-enable MD012 -->

**[⬆ về đầu trang](#table-of-contents)**

## <a name="commas">Các Dấu phẩy</a>

  <a name="commas--leading-trailing"></a><a name="19.1"></a>
  - [20.1](#commas--leading-trailing) Các dấu phẩy ở đầu: **Đừng!** eslint: [`comma-style`](https://eslint.org/docs/rules/comma-style.html)

    ``` javascript
    // không tốt
    const story = [
        once
      , upon
      , aTime
    ];

    // tốt
    const story = [
      once,
      upon,
      aTime,
    ];

    // không tốt
    const hero = {
        firstName: 'Ada'
      , lastName: 'Lovelace'
      , birthYear: 1815
      , superPower: 'máy tính'
    };

    // tốt
    const hero = {
      firstName: 'Ada',
      lastName: 'Lovelace',
      birthYear: 1815,
      superPower: 'máy tính',
    };
    ```

  <a name="commas--dangling"></a><a name="19.2"></a>
  - [20.2](#commas--dangling) Thêm một dấu phẩy ở cuối: **Đúng đó!** eslint: [`comma-dangle`](https://eslint.org/docs/rules/comma-dangle.html)

    > Tại sao? Điều này làm cho các so sánh git gọn gàng hơn. Ngoài ra, các trình dịch mã như Babel sẽ xóa các dấu phẩy ở cuối trong mã được dịch, có nghĩa là bạn không cần lo lắng về [vấn đề của dấu phẩy ở cuối](https://github.com/airbnb/javascript/blob/es5-deprecated/es5/README.md#commas) trên các trình duyệt cũ.

    ```diff
    // không tốt - so sánh git khi không có dấu phẩy ở cuối
    const hero = {
         firstName: 'Florence',
    -    lastName: 'Nightingale'
    +    lastName: 'Nightingale',
    +    inventorOf: ['coxcomb chart', 'modern nursing']
    };

    // tốt - so sánh git khi có các dấu phẩy ở cuối
    const hero = {
         firstName: 'Florence',
         lastName: 'Nightingale',
    +    inventorOf: ['coxcomb chart', 'modern nursing'],
    };
    ```

    ```  javascript
    // không tốt
    const hero = {
      firstName: 'Dana',
      lastName: 'Scully'
    };

    const heroes = [
      'Batman',
      'Superman'
    ];

    // tốt
    const hero = {
      firstName: 'Dana',
      lastName: 'Scully',
    };

    const heroes = [
      'Batman',
      'Superman',
    ];

    // không tốt
    function createHero(
      firstName,
      lastName,
      inventorOf
    ) {
      // không làm gì cả
    }

    // tốt
    function createHero(
      firstName,
      lastName,
      inventorOf,
    ) {
      // không làm gì cả
    }

    // tốt (lưu ý là không được đặt dấu phẩy sau phần từ "còn-lại")
    function createHero(
      firstName,
      lastName,
      inventorOf,
      ...heroArgs
    ) {
      // không làm gì cả
    }

    // không tốt
    createHero(
      firstName,
      lastName,
      inventorOf
    );

    // tốt
    createHero(
      firstName,
      lastName,
      inventorOf,
    );

    // tốt (lưu ý là không được đặt dấu phẩy sau phần từ "còn-lại")
    createHero(
      firstName,
      lastName,
      inventorOf,
      ...heroArgs
    );
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="semicolons">Các Dấu chấm phẩy</a>

  <a name="semicolons--required"></a><a name="20.1"></a>
  - [21.1](#semicolons--required) **Dĩ nhiên.** eslint: [`semi`](https://eslint.org/docs/rules/semi.html)

    > Tại sao? Khi JavaScript gặp một dấu ngắt dòng mà không có dấu chấm phẩy, nó sử dụng một bộ quy tắc gọi là [Quy tắc thêm dấu chấm phẩy tự động](https://tc39.github.io/ecma262/#sec-automatic-semicolon-insertion) để xác định xem dấu ngắt dòng có phải là kết thúc của một câu lệnh hay không, và (như cái tên gợi ý) đặt một dấu chấn phẩy vào mã của bạn, trước dấu ngắt dòng, nếu nó cho rằng nên làm vậy. Quy tắc thêm dấu chấm phẩy tự động có một vài hành vi lập dị, và mã của bạn sẽ hỏng nếu JavaScript hiểu sai dấu ngắt dòng của bạn. Những quy tắc này ngày càng trở nên phức tạp khi các tính năng mới được bổ sung vào JavaScript. Việc kết thúc các câu lệnh một cách rõ ràng và thiết lập trình phân tích mã của bạn bắt các lỗi thiếu dấu phẩy sẽ giúp bạn tránh được các vấn đề.

    ``` javascript
    // không tốt - ném ra một ngoại lệ
    const luke = {}
    const leia = {}
    [luke, leia].forEach(jedi => jedi.father = 'vader')

    // không tốt - ngém ra một ngoại lệ
    const reaction = "Không! Không thể nào!"
    (async function meanwhileOnTheFalcon() {
      // xử lý `leia`, `lando`, `chewie`, `r2`, `c3p0`
      // ...
    }())

    // không tốt - trả về `undefined` thay vì giá trị ở dòng tiếp theo - điều luôn xảy ra khi `return` nằm một mình một dòng, do Quy tắc thêm dấu chấm phẩy tự động!
    function foo() {
      return
        'search your feelings, you know it to be foo'
    }

    // tốt
    const luke = {};
    const leia = {};
    [luke, leia].forEach((jedi) => {
      jedi.father = 'vader';
    });

    // tốt
    const reaction = "Không! Không thể nào!";
    (async function meanwhileOnTheFalcon() {
      // xử lý `leia`, `lando`, `chewie`, `r2`, `c3p0`
      // ...
    }());

    // tốt
    function foo() {
      return 'search your feelings, you know it to be foo';
    }
    ```

    [Đọc thêm](https://stackoverflow.com/questions/7365172/semicolon-before-self-invoking-function/7365214#7365214).

**[⬆ về đầu trang](#table-of-contents)**

## <a name="type-casting--coercion">Sự ép kiểu</a>

  <a name="coercion--explicit"></a><a name="21.1"></a>
  - [22.1](#coercion--explicit) Thực hiện ép kiểu ở đầu mỗi câu lệnh.

  <a name="coercion--strings"></a><a name="21.2"></a>
  - [22.2](#coercion--strings) Đối với các chuỗi: eslint: [`no-new-wrappers`](https://eslint.org/docs/rules/no-new-wrappers)

    ``` javascript
    // => this.reviewScore = 9;

    // không tốt
    const totalScore = new String(this.reviewScore); // typeof totalScore là "object", không phải "string"

    // không tốt
    const totalScore = this.reviewScore + ''; // cái này gọi this.reviewScore.valueOf()

    // không tốt
    const totalScore = this.reviewScore.toString(); // không chắc chắn sẽ thu được một chuỗi

    // tốt
    const totalScore = String(this.reviewScore);
    ```

  <a name="coercion--numbers"></a><a name="21.3"></a>
  - [22.3](#coercion--numbers) Đối với các số: Sử dụng `Number` để ép kiểu và `parseInt` luôn phải được dùng với một cơ số. eslint: [`radix`](https://eslint.org/docs/rules/radix) [`no-new-wrappers`](https://eslint.org/docs/rules/no-new-wrappers)

    ``` javascript
    const inputValue = '4';

    // không tốt
    const val = new Number(inputValue);

    // không tốt
    const val = +inputValue;

    // không tốt
    const val = inputValue >> 0;

    // không tốt
    const val = parseInt(inputValue);

    // tốt
    const val = Number(inputValue);

    // tốt
    const val = parseInt(inputValue, 10);
    ```

  <a name="coercion--comment-deviations"></a><a name="21.4"></a>
  - [22.4](#coercion--comment-deviations) Nếu, vì bất cứ lý do gì, bạn đang làm một điều gì đó thật điên và bạn gặp nghẽn cổ chai do `parseInt`, và bạn cần sử dụng phép dịch chuyển bit vì [các lý do hiệu suất](https://jsperf.com/coercion-vs-casting/3), nhớ để lại một chú thích để giải thích về thứ bạn đang làm và tại sao bạn làm vậy.

    ``` javascript
    // tốt
    /**
     * parseInt là lý do khiến mã của tôi chạy chậm.
     * Việc áp dụng phép dịch chuyển bit cho một chuỗi
     * để ép nó sang kiểu số nhanh hơn nhiều.
     */
    const val = inputValue >> 0;
    ```

  <a name="coercion--bitwise"></a><a name="21.5"></a>
  - [22.5](#coercion--bitwise) **Lưu ý:** Cẩn thận khi sử dụng các phép dịch chuyển bit. Các số được biểu diễn dưới dạng các [giá trị 64-bit](https://es5.github.io/#x4.3.19), nhưng các phép dịch chuyển bit luôn trả về một số nguyên 32-bit ([nguồn](https://es5.github.io/#x11.7)). Phép dịch chuyển bit cũng có thể dẫn đến các hành vi không mong đợi đối với các giá trị lớn hơn 32 bit. [Cuộc thảo luận](https://github.com/airbnb/javascript/issues/109). Số nguyên có dấu 32-bit lớn nhất là 2,147,483,647:

    ``` javascript
    2147483647 >> 0; // => 2147483647
    2147483648 >> 0; // => -2147483648
    2147483649 >> 0; // => -2147483647
    ```

  <a name="coercion--booleans"></a><a name="21.6"></a>
  - [22.6](#coercion--booleans) Đối với các boolean: eslint: [`no-new-wrappers`](https://eslint.org/docs/rules/no-new-wrappers)

    ``` javascript
    const age = 0;

    // không tốt
    const hasAge = new Boolean(age);

    // tốt
    const hasAge = Boolean(age);

    // tốt nhất
    const hasAge = !!age;
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="naming-conventions">Các Quy ước Đặt tên</a>

  <a name="naming--descriptive"></a><a name="22.1"></a>
  - [23.1](#naming--descriptive) Tránh sử dụng các tên chỉ có một chữ cái. Hãy đặt những cái tên thật ý nghĩa. eslint: [`id-length`](https://eslint.org/docs/rules/id-length)

    ``` javascript
    // không tốt
    function q() {
      // ...
    }

    // tốt
    function query() {
      // ...
    }
    ```

  <a name="naming--camelCase"></a><a name="22.2"></a>
  - [23.2](#naming--camelCase) Sử dụng camelCase khi đặt tên các đối tượng, các hàm và các thực thể. eslint: [`camelcase`](https://eslint.org/docs/rules/camelcase.html)

    ``` javascript
    // không tốt
    const OBJEcttsssss = {};
    const this_is_my_object = {};
    function c() {}

    // tốt
    const thisIsMyObject = {};
    function thisIsMyFunction() {}
    ```

  <a name="naming--PascalCase"></a><a name="22.3"></a>
  - [23.3](#naming--PascalCase) Sử dụng PascalCase chỉ khi đặt tên các hàm tạo hay các lớp. eslint: [`new-cap`](https://eslint.org/docs/rules/new-cap.html)

    ``` javascript
    // không tốt
    function user(options) {
      this.name = options.name;
    }

    const bad = new user({
      name: 'đừnggg',
    });

    // tốt
    class User {
      constructor(options) {
        this.name = options.name;
      }
    }

    const good = new User({
      name: 'đúng nè',
    });
    ```

  <a name="naming--leading-underscore"></a><a name="22.4"></a>
  - [23.4](#naming--leading-underscore) Không sử dụng các dấu gạch dưới ở đằng trước hoặc đằng sau. eslint: [`no-underscore-dangle`](https://eslint.org/docs/rules/no-underscore-dangle.html)

    > Tại sao? JavaScript không có khái niệm về tính riêng tư khi nói đến các thuộc tính hay các phương thức. Tuy rằng một dấu gạch dưới đặt ở đằng trước là một quy ước chung mang nghĩa “riêng tư”, thực tế, các thuộc tính trên đều hoàn toàn công khai, và vì vậy, là các thành phần trong API của bạn. Quy ước này có thể khiến các nhà phát triển nghĩ, một cách sai lầm, rằng một sự thay đổi chẳng làm hỏng điều gì, hoặc không cần thiết phải kiểm thử. tl;dr: nếu bạn muốn thứ gì đó thật “riêng tư”, sự tồn tại của nó phải được giấu đi.

    ``` javascript
    // không tốt
    this.__firstName__ = 'Panda';
    this.firstName_ = 'Panda';
    this._firstName = 'Panda';

    // tốt
    this.firstName = 'Panda';

    // tốt, đối với các môi trường hỗ trợ WeakMap
    // xem https://kangax.github.io/compat-table/es6/#test-WeakMap
    const firstNames = new WeakMap();
    firstNames.set(this, 'Panda');
    ```

  <a name="naming--self-this"></a><a name="22.5"></a>
  - [23.5](#naming--self-this) Đừng lưu các tham chiếu đến `this`. Hãy sử dụng hàm mũi tên hoặc [Function#bind](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind).

    ``` javascript
    // không tốt
    function foo() {
      const self = this;
      return function () {
        console.log(self);
      };
    }

    // không tốt
    function foo() {
      const that = this;
      return function () {
        console.log(that);
      };
    }

    // tốt
    function foo() {
      return () => {
        console.log(this);
      };
    }
    ```

  <a name="naming--filename-matches-export"></a><a name="22.6"></a>
  - [23.6](#naming--filename-matches-export) Phần tên của một tên tệp nên giống với địa chỉ xuất mặc định của tệp đó.

    ``` javascript
    // file 1 contents
    class CheckBox {
      // ...
    }
    export default CheckBox;

    // file 2 contents
    export default function fortyTwo() { return 42; }

    // file 3 contents
    export default function insideDirectory() {}

    // in some other file
    // không tốt
    import CheckBox from './checkBox'; // nhập PascalCase, tên camelCase
    import FortyTwo from './FortyTwo'; // nhập/tên PascalCase, xuất camelCase
    import InsideDirectory from './InsideDirectory'; // nhập/tên PascalCase, xuất camelCase

    // không tốt
    import CheckBox from './check_box'; // nhập/xuất PascalCase, tên snake_case
    import forty_two from './forty_two'; // nhập/tên snake_case, xuất camelCase
    import inside_directory from './inside_directory'; // nhập snake_case, xuất camelCase
    import index from './inside_directory/index'; // ghi tên tệp index
    import insideDirectory from './insideDirectory/index'; // ghi tên tệp index

    // tốt
    import CheckBox from './CheckBox'; // xuất/nhập/tên PascalCase
    import fortyTwo from './fortyTwo'; // xuất/nhập/tên camelCase
    import insideDirectory from './insideDirectory'; // xuất/nhập/tên camelCase; ngầm định "index"
    // ^ hỗ trợ cả insideDirectory.js và insideDirectory/index.js
    ```

  <a name="naming--camelCase-default-export"></a><a name="22.7"></a>
  - [23.7](#naming--camelCase-default-export) Sử dụng camelCase khi xuất mặc định một hàm. Tên tệp nên trùng với tên hàm.

    ``` javascript
    function makeStyleGuide() {
      // ...
    }

    export default makeStyleGuide;
    ```

  <a name="naming--PascalCase-singleton"></a><a name="22.8"></a>
  - [23.8](#naming--PascalCase-singleton) Sử dụng PascalCase khi xuất mặc định một hàm tạo / lớp / đối tượng độc nhật / một thư viện các hàm / đối tượng trần.

    ``` javascript
    const AirbnbStyleGuide = {
      es6: {
      },
    };

    export default AirbnbStyleGuide;
    ```

  <a name="naming--Acronyms-and-Initialisms"></a>
  - [23.9](#naming--Acronyms-and-Initialisms) Các từ viết tắt nên được viết hoa hoặc viết thường toàn bộ.

    > Tại sao? Các tên dùng để đọc, không phải để giải thích thuật toán.

    ``` javascript
    // không tốt
    import SmsContainer from './containers/SmsContainer';

    // không tốt
    const HttpRequests = [
      // ...
    ];

    // tốt
    import SMSContainer from './containers/SMSContainer';

    // tốt
    const HTTPRequests = [
      // ...
    ];

    // như này cũng tốt
    const httpRequests = [
      // ...
    ];

    // tốt nhất
    import TextMessageContainer from './containers/TextMessageContainer';

    // tốt nhất
    const requests = [
      // ...
    ];
    ```

  <a name="naming--uppercase"></a>
  - [23.10](#naming--uppercase) Bạn có chọn viết hoa một hằng chỉ khi hằng đó (1) được xuất, và (2) một lập trình viên có thể tin tưởng rằng nó (và các thuộc tính của nó) là bất biến.

    > Tại sao? Đây là một công cụ khác để hỗ trợ chúng ta trong các hoàn cảnh mà một lập trình viên có thể không chắc chắn là một biến có bị thay đổi hay chưa. UPPERCASE_VARIABLES đang cho lập trình viên đó biết là biến này (và thuộc tính của nó) không có thay đổi gì hết.
    - Thế còn các `const`? - Điều này là không cần thiết, vì việc viết hoa không nên được sử dụng cho các hằng ở trong cùng một tệp. Nó chỉ nên dùng cho các hằng được xuất.
    - Thế còn một đối tượng được xuất thì sao? - Chỉ viết hoa ở hàng cao nhất của đối tượng xuất (kiểu như: `EXPORTED_OBJECT.key`) và đảm bảo rằng những thuộc tính của nó không thay đổi.

    ``` javascript
    // không tốt
    const PRIVATE_VARIABLE = 'không nên viết hoa bừa bãi các biến trong một tệp';

    // không tốt
    export const THING_TO_BE_CHANGED = 'rõ ràng không nên viết hoa';

    // không tốt
    export let REASSIGNABLE_VARIABLE = 'đừng có sử dụng let với tên viết hóa';

    // ---

    // được cho phép, nhưng không không rõ về mặt ngữ nghĩa
    export const apiKey = 'SOMEKEY';

    // tốt hơn hầu hết các trường hợp khác
    export const API_KEY = 'SOMEKEY';

    // ---

    // không tốt - viết hoa không cần thiết chẳng cung cấp gì trị gì về mặt ngữ nghĩa
    export const MAPPING = {
      KEY: 'giá trị'
    };

    // tốt
    export const MAPPING = {
      key: 'giá trị'
    };
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="accessors">Các Hàm truy cập</a>

  <a name="accessors--not-required"></a><a name="23.1"></a>
  - [24.1](#accessors--not-required) Các hàm truy cập cho các thuộc tình là không bắt buộc.

  <a name="accessors--no-getters-setters"></a><a name="23.2"></a>
  - [24.2](#accessors--no-getters-setters) Không sử dụng hàm đọc/hàm ghi của JavaScript vì chúng gây ra các hiệu ứng phụ không mong muốn và khó để kiểm thử, bảo trì, và hình dung. Thay vào đó, nếu bạn muốn tạo hàm truy cập, sử dụng `getVal()` và `setVal('hello')`.

    ``` javascript
    // không tốt
    class Dragon {
      get age() {
        // ...
      }

      set age(value) {
        // ...
      }
    }

    // tốt
    class Dragon {
      getAge() {
        // ...
      }

      setAge(value) {
        // ...
      }
    }
    ```

  <a name="accessors--boolean-prefix"></a><a name="23.3"></a>
  - [24.3](#accessors--boolean-prefix) Nếu thuộc tính/phương thức là một `boolean`, dùng `isVal()` hoặc `hasVal()`.

    ``` javascript
    // không tốt
    if (!dragon.age()) {
      return false;
    }

    // tốt
    if (!dragon.hasAge()) {
      return false;
    }
    ```

  <a name="accessors--consistent"></a><a name="23.4"></a>
  - [24.4](#accessors--consistent) Có thể dùng các hàm `get()` và `set()`, nhưng nhớ là phải nhất quán.

    ``` javascript
    class Jedi {
      constructor(options = {}) {
        const lightsaber = options.lightsaber || 'xanh dương';
        this.set('lightsaber', lightsaber);
      }

      set(key, val) {
        this[key] = val;
      }

      get(key) {
        return this[key];
      }
    }
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="events">Các Sự kiện</a>

  <a name="events--hash"></a><a name="24.1"></a>
  - [25.1](#events--hash) Khi gắn các trọng tải dữ liệu cho các sự kiện (dù là các sự kiện DOM hay thứ gì đó tư hữu hơn như các sự kiện trong Backbone), hãy truyền vào một đối tượng nguyên văn (hay còn gọi là "giá trị băm") thay vì giá trị gốc. Điều này cho phép những người đóng góp sau này có thể thêm dữ liệu vào trọng tải mà không cần phải tìm và cập nhật mỗi hàm xử lý cho sự kiện. Ví dụ, thay vì:

    ``` javascript
    // không tốt
    $(this).trigger('listingUpdated', listing.id);

    // ...

    $(this).on('listingUpdated', (e, listingID) => {
      // làm gì đó với listingID
    });
    ```

    hãy dùng:

    ``` javascript
    // tốt
    $(this).trigger('listingUpdated', { listingID: listing.id });

    // ...

    $(this).on('listingUpdated', (e, data) => {
      // làm gì đó với listingID
    });
    ```

  **[⬆ về đầu trang](#table-of-contents)**

## <a name="jquery">jQuery</a>

  <a name="jquery--dollar-prefix"></a><a name="25.1"></a>
  - [26.1](#jquery--dollar-prefix) Bắt đầu các biến lưu các đối tượng jQuery với `$`.

    ``` javascript
    // không tốt
    const sidebar = $('.sidebar');

    // tốt
    const $sidebar = $('.sidebar');

    // tốt
    const $sidebarBtn = $('.sidebar-btn');
    ```

  <a name="jquery--cache"></a><a name="25.2"></a>
  - [26.2](#jquery--cache) Lưu tạm các truy vấn jQuery.

    ``` javascript
    // không tốt
    function setSidebar() {
      $('.sidebar').hide();

      // ...

      $('.sidebar').css({
        'background-color': 'pink',
      });
    }

    // tốt
    function setSidebar() {
      const $sidebar = $('.sidebar');
      $sidebar.hide();

      // ...

      $sidebar.css({
        'background-color': 'pink',
      });
    }
    ```

  <a name="jquery--queries"></a><a name="25.3"></a>
  - [26.3](#jquery--queries) Với các truy vấn, hãy sử dụng truy vấn xếp tầng `$('.sidebar ul')` hoặc cha > con `$('.sidebar > ul')`. [jsPerf](http://jsperf.com/jquery-find-vs-context-sel/16)

  <a name="jquery--find"></a><a name="25.4"></a>
  - [26.4](#jquery--find) Sử dụng `find` với một phạm vi đối tượng jQuery cho các truy vấn.

    ``` javascript
    // không tốt
    $('ul', '.sidebar').hide();

    // không tốt
    $('.sidebar').find('ul').hide();

    // tốt
    $('.sidebar ul').hide();

    // tốt
    $('.sidebar > ul').hide();

    // tốt
    $sidebar.find('ul').hide();
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="ecmascript-5-compatibility">Tính tương thích của ECMAScript 5</a>

  <a name="es5-compat--kangax"></a><a name="26.1"></a>
  - [27.1](#es5-compat--kangax) Tham khảo [bảng tính tương thích](https://kangax.github.io/es5-compat-table/) ES5 của [Kangax](https://twitter.com/kangax/).

**[⬆ về đầu trang](#table-of-contents)**

<a name="ecmascript-6-styles"></a>
## <a name="ecmascript-6-es-2015-styles">Lối viết ECMAScript 6+ (ES 2015+)</a>

  <a name="es6-styles"></a><a name="27.1"></a>
  - [28.1](#es6-styles) Đây là một bộ sưu tập các liên kết tới các tính năng khác nhau của ES6+.

1. [Các Hàm mũi tên](#arrow-functions)
1. [Các Lớp](#classes--constructors)
1. [Cú pháp Định nghĩa Phương thức Rút gọn](#es6-object-shorthand)
1. [Cú pháp Định nghĩa Thuộc tính Rút gọn](#es6-object-concise)
1. [Các Tên Được tính của Thuộc tính](#es6-computed-properties)
1. [Các Mẫu chuỗi](#es6-template-literals)
1. [Trích xuất](#destructuring)
1. [Các Tham số Mặc định](#es6-default-parameters)
1. [Còn-lại](#es6-rest)
1. [Liệt kê Mảng](#es6-array-spreads)
1. [Let và Const](#references)
1. [Toán tử Lũy thừa](#es2016-properties--exponentiation-operator)
1. [Các Đối tượng duyệt và các Hàm sinh trị](#iterators-and-generators)
1. [Các Mô-đun](#modules)

  <a name="tc39-proposals"></a>
  - [28.2](#tc39-proposals) Không sử dụng [các đề xuất TC39](https://github.com/tc39/proposals) mà chưa đến giai đoạn 3.

    > Tại sao? [Chúng chưa được hoàn thiện](https://tc39.github.io/process-document/), và chúng có thể thay đổi bất cứ lúc nào hoặc bị rút lại hoàn toàn. Chúng ta muốn sử dụng JavaScript, mà các đề xuất thì chưa phải là JavaScript.

**[⬆ về đầu trang](#table-of-contents)**

## <a name="standard-library">Thư viện Tiêu Chuẩn</a>

  [Thư viện tiêu chuẩn](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects)
  chứa các hàm tiện ích không hoạt động đúng lắm nhưng vẫn tồn tại vì các lý do cũ.

  <a name="standard-library--isnan"></a>
  - [29.1](#standard-library--isnan) Sử dụng `Number.isNaN` thay vì hàm toàn cục `isNaN`.
    eslint: [`no-restricted-globals`](https://eslint.org/docs/rules/no-restricted-globals)

    > Tại sao? Hàm toàn cục `isNaN` ép các giá trị không phải số thành số và trả về true cho tất cả những gì mà bị ép thành NaN.
    > Nếu đây là hành vi mong muốn, hãy khiến nó được biểu đạt rõ ràng.

    ``` javascript
    // không tốt
    isNaN('1.2'); // false
    isNaN('1.2.3'); // true

    // tốt
    Number.isNaN('1.2.3'); // false
    Number.isNaN(Number('1.2.3')); // true
    ```

  <a name="standard-library--isfinite"></a>
  - [29.2](#standard-library--isfinite) Sử dụng `Number.isFinite` thay vì hàm toàn cục `isFinite`.
    eslint: [`no-restricted-globals`](https://eslint.org/docs/rules/no-restricted-globals)

    > Tại sao? Hàm toàn cục `isFinite` ép các giá trị không phải số thành số và trả về true cho tất cả những gì bị ép thành một số mà không phải là vô hạn.
    > Nếu đây là hành vi mong muốn, hãy khiến nó được biểu đạt rõ ràng.

    ``` javascript
    // không tốt
    isFinite('2e3'); // true

    // tốt
    Number.isFinite('2e3'); // false
    Number.isFinite(parseInt('2e3', 10)); // true
    ```

**[⬆ về đầu trang](#table-of-contents)**

## <a name="testing">Sự kiểm thử</a>

  <a name="testing--yup"></a><a name="28.1"></a>
  - [30.1](#testing--yup) **Có chứ.**

    ``` javascript
    function foo() {
      return true;
    }
    ```

  <a name="testing--for-real"></a><a name="28.2"></a>
  - [30.2](#testing--for-real) **Không, nhưng nghiêm túc này**:
    - Dù bạn dùng nền tảng kiểm thử nào thì bạn cũng nên viết các kiểm thử!
    - Cố gắng viết thật nhiều các hàm thuần, nhỏ và giảm thiểu số các sự biến đổi.
    - Cẩn thận với các giả lập mô-đun và đối tượng - chúng có thể khiến các chương trình kiểm thử của bạn dễ vỡ.
    - Chúng tôi chủ yếu sử dụng [`mocha`](https://www.npmjs.com/package/mocha) và [`jest`](https://www.npmjs.com/package/jest) tại Airbnb. [`tape`](https://www.npmjs.com/package/tape) cũng đôi khi được sử dụng cho các mô-đun nhỏ và tách biệt.
    - 100% độ bao phủ kiểm thử là một mục tiêu tốt để phấn đấu, dù không phải lúc nào cũng khả thi.
    - Mỗi khi bạn sửa một lỗi, _viết một kiểm thử hồi quy_. Một lỗi được sửa nhưng không được viết kiểm thử lại gần như chắc chắn sẽ lại hỏng trong tương lai.

**[⬆ về đầu trang](#table-of-contents)**

## <a name="performance">Hiệu suất</a>

  - [On Layout & Web Performance](https://www.kellegous.com/j/2013/01/26/layout-performance/)
  - [String vs Array Concat](https://jsperf.com/string-vs-array-concat/2)
  - [Try/Catch Cost In a Loop](https://jsperf.com/try-catch-in-loop-cost)
  - [Bang Function](https://jsperf.com/bang-function)
  - [jQuery Find vs Context, Selector](https://jsperf.com/jquery-find-vs-context-sel/13)
  - [innerHTML vs textContent for script text](https://jsperf.com/innerhtml-vs-textcontent-for-script-text)
  - [Long String Concatenation](https://jsperf.com/ya-string-concat)
  - [Are Javascript functions like `map()`, `reduce()`, and `filter()` optimized for traversing arrays?](https://www.quora.com/JavaScript-programming-language-Are-Javascript-functions-like-map-reduce-and-filter-already-optimized-for-traversing-array/answer/Quildreen-Motta)
  - Đang tải...

**[⬆ về đầu trang](#table-of-contents)**

## <a name="resources">Các Tài nguyên</a>

**Học ES6+**

  - [Latest ECMA spec](https://tc39.github.io/ecma262/)
  - [ExploringJS](http://exploringjs.com/)
  - [ES6 Compatibility Table](https://kangax.github.io/compat-table/es6/)
  - [Comprehensive Overview of ES6 Features](http://es6-features.org/)

**Đọc cái này đi**

  - [Standard ECMA-262](http://www.ecma-international.org/ecma-262/6.0/index.html)

**Các công cụ**

  - Trình phân tích lối viết mã
    - [ESlint](https://eslint.org/) - [Lối viết của Airbnb .eslintrc](https://github.com/airbnb/javascript/blob/master/linters/.eslintrc)
    - [JSHint](http://jshint.com/) - [Lối viết của Airbnb .jshintrc](https://github.com/airbnb/javascript/blob/master/linters/.jshintrc)
  - Gói Neutrino - [@neutrinojs/airbnb](https://neutrinojs.org/packages/airbnb/)

**Các Định hướng Lối viết Khác**

  - [Google JavaScript Style Guide](https://google.github.io/styleguide/javascriptguide.xml)
  - [jQuery Core Style Guidelines](https://contribute.jquery.org/style-guide/js/)
  - [Principles of Writing Consistent, Idiomatic JavaScript](https://github.com/rwaldron/idiomatic.js)
  - [StandardJS](https://standardjs.com)

**Các Lối viết Khác**

  - [Naming this in nested functions](https://gist.github.com/cjohansen/4135065) - Christian Johansen
  - [Conditional Callbacks](https://github.com/airbnb/javascript/issues/52) - Ross Allen
  - [Popular JavaScript Coding Conventions on GitHub](http://sideeffect.kr/popularconvention/#javascript) - JeongHoon Byun
  - [Multiple var statements in JavaScript, not superfluous](http://benalman.com/news/2012/05/multiple-var-statements-javascript/) - Ben Alman

**Đọc thêm**

  - [Understanding JavaScript Closures](https://javascriptweblog.wordpress.com/2010/10/25/understanding-javascript-closures/) - Angus Croll
  - [Basic JavaScript for the impatient programmer](http://www.2ality.com/2013/06/basic-javascript.html) - Dr. Axel Rauschmayer
  - [You Might Not Need jQuery](http://youmightnotneedjquery.com/) - Zack Bloom & Adam Schwartz
  - [ES6 Features](https://github.com/lukehoban/es6features) - Luke Hoban
  - [Frontend Guidelines](https://github.com/bendc/frontend-guidelines) - Benjamin De Cock

**Các Tựa sách**

  - [JavaScript: The Good Parts](https://www.amazon.com/JavaScript-Good-Parts-Douglas-Crockford/dp/0596517742) - Douglas Crockford
  - [JavaScript Patterns](https://www.amazon.com/JavaScript-Patterns-Stoyan-Stefanov/dp/0596806752) - Stoyan Stefanov
  - [Pro JavaScript Design Patterns](https://www.amazon.com/JavaScript-Design-Patterns-Recipes-Problem-Solution/dp/159059908X) - Ross Harmes and Dustin Diaz
  - [High Performance Web Sites: Essential Knowledge for Front-End Engineers](https://www.amazon.com/High-Performance-Web-Sites-Essential/dp/0596529309) - Steve Souders
  - [Maintainable JavaScript](https://www.amazon.com/Maintainable-JavaScript-Nicholas-C-Zakas/dp/1449327680) - Nicholas C. Zakas
  - [JavaScript Web Applications](https://www.amazon.com/JavaScript-Web-Applications-Alex-MacCaw/dp/144930351X) - Alex MacCaw
  - [Pro JavaScript Techniques](https://www.amazon.com/Pro-JavaScript-Techniques-John-Resig/dp/1590597273) - John Resig
  - [Smashing Node.js: JavaScript Everywhere](https://www.amazon.com/Smashing-Node-js-JavaScript-Everywhere-Magazine/dp/1119962595) - Guillermo Rauch
  - [Secrets of the JavaScript Ninja](https://www.amazon.com/Secrets-JavaScript-Ninja-John-Resig/dp/193398869X) - John Resig and Bear Bibeault
  - [Human JavaScript](http://humanjavascript.com/) - Henrik Joreteg
  - [Superhero.js](http://superherojs.com/) - Kim Joar Bekkelund, Mads Mobæk, & Olav Bjorkoy
  - [JSBooks](http://jsbooks.revolunet.com/) - Julien Bouquillon
  - [Third Party JavaScript](https://www.manning.com/books/third-party-javascript) - Ben Vinegar and Anton Kovalyov
  - [Effective JavaScript: 68 Specific Ways to Harness the Power of JavaScript](http://amzn.com/0321812182) - David Herman
  - [Eloquent JavaScript](http://eloquentjavascript.net/) - Marijn Haverbeke
  - [You Don’t Know JS: ES6 & Beyond](http://shop.oreilly.com/product/0636920033769.do) - Kyle Simpson

**Các Bài viết**

  - [JavaScript Weekly](http://javascriptweekly.com/)
  - [JavaScript, JavaScript...](https://javascriptweblog.wordpress.com/)
  - [Bocoup Weblog](https://bocoup.com/weblog)
  - [Adequately Good](http://www.adequatelygood.com/)
  - [NCZOnline](https://www.nczonline.net/)
  - [Perfection Kills](http://perfectionkills.com/)
  - [Ben Alman](http://benalman.com/)
  - [Dmitry Baranovskiy](http://dmitry.baranovskiy.com/)
  - [nettuts](http://code.tutsplus.com/?s=javascript)

**Các Bản phát thanh**

  - [JavaScript Air](https://javascriptair.com/)
  - [JavaScript Jabber](https://devchat.tv/js-jabber/)

**[⬆ về đầu trang](#table-of-contents)**

## <a name="in-the-wild">Thực tế Áp dụng</a>

  Đây là danh sách những tổ chức sử dụng định hướng lối viết này. Gửi cho chúng tôi một yêu cầu kéo và chúng tôi sẽ thêm bạn vào danh sách.

  - **123erfasst**: [123erfasst/javascript](https://github.com/123erfasst/javascript)
  - **3blades**: [3Blades](https://github.com/3blades)
  - **4Catalyzer**: [4Catalyzer/javascript](https://github.com/4Catalyzer/javascript)
  - **Aan Zee**: [AanZee/javascript](https://github.com/AanZee/javascript)
  - **Adult Swim**: [adult-swim/javascript](https://github.com/adult-swim/javascript)
  - **Airbnb**: [airbnb/javascript](https://github.com/airbnb/javascript)
  - **AltSchool**: [AltSchool/javascript](https://github.com/AltSchool/javascript)
  - **Apartmint**: [apartmint/javascript](https://github.com/apartmint/javascript)
  - **Ascribe**: [ascribe/javascript](https://github.com/ascribe/javascript)
  - **Avalara**: [avalara/javascript](https://github.com/avalara/javascript)
  - **Avant**: [avantcredit/javascript](https://github.com/avantcredit/javascript)
  - **Axept**: [axept/javascript](https://github.com/axept/javascript)
  - **BashPros**: [BashPros/javascript](https://github.com/BashPros/javascript)
  - **Billabong**: [billabong/javascript](https://github.com/billabong/javascript)
  - **Bisk**: [bisk](https://github.com/Bisk/)
  - **Bonhomme**: [bonhommeparis/javascript](https://github.com/bonhommeparis/javascript)
  - **Brainshark**: [brainshark/javascript](https://github.com/brainshark/javascript)
  - **CaseNine**: [CaseNine/javascript](https://github.com/CaseNine/javascript)
  - **Cerner**: [Cerner](https://github.com/cerner/)
  - **Chartboost**: [ChartBoost/javascript-style-guide](https://github.com/ChartBoost/javascript-style-guide)
  - **Coeur d'Alene Tribe**: [www.cdatribe-nsn.gov](https://www.cdatribe-nsn.gov)
  - **ComparaOnline**: [comparaonline/javascript](https://github.com/comparaonline/javascript-style-guide)
  - **Compass Learning**: [compasslearning/javascript-style-guide](https://github.com/compasslearning/javascript-style-guide)
  - **DailyMotion**: [dailymotion/javascript](https://github.com/dailymotion/javascript)
  - **DoSomething**: [DoSomething/eslint-config](https://github.com/DoSomething/eslint-config)
  - **Digitpaint** [digitpaint/javascript](https://github.com/digitpaint/javascript)
  - **Drupal**: [www.drupal.org](https://www.drupal.org/project/drupal)
  - **Ecosia**: [ecosia/javascript](https://github.com/ecosia/javascript)
  - **Evernote**: [evernote/javascript-style-guide](https://github.com/evernote/javascript-style-guide)
  - **Evolution Gaming**: [evolution-gaming/javascript](https://github.com/evolution-gaming/javascript)
  - **EvozonJs**: [evozonjs/javascript](https://github.com/evozonjs/javascript)
  - **ExactTarget**: [ExactTarget/javascript](https://github.com/ExactTarget/javascript)
  - **Expensify** [Expensify/Style-Guide](https://github.com/Expensify/Style-Guide/blob/master/javascript.md)
  - **Flexberry**: [Flexberry/javascript-style-guide](https://github.com/Flexberry/javascript-style-guide)
  - **Gawker Media**: [gawkermedia](https://github.com/gawkermedia/)
  - **General Electric**: [GeneralElectric/javascript](https://github.com/GeneralElectric/javascript)
  - **Generation Tux**: [GenerationTux/javascript](https://github.com/generationtux/styleguide)
  - **GoodData**: [gooddata/gdc-js-style](https://github.com/gooddata/gdc-js-style)
  - **GreenChef**: [greenchef/javascript](https://github.com/greenchef/javascript)
  - **Grooveshark**: [grooveshark/javascript](https://github.com/grooveshark/javascript)
  - **Grupo-Abraxas**: [Grupo-Abraxas/javascript](https://github.com/Grupo-Abraxas/javascript)
  - **Honey**: [honeyscience/javascript](https://github.com/honeyscience/javascript)
  - **How About We**: [howaboutwe/javascript](https://github.com/howaboutwe/javascript-style-guide)
  - **Huballin**: [huballin](https://github.com/huballin/)
  - **HubSpot**: [HubSpot/javascript](https://github.com/HubSpot/javascript)
  - **Hyper**: [hyperoslo/javascript-playbook](https://github.com/hyperoslo/javascript-playbook/blob/master/style.md)
  - **InterCity Group**: [intercitygroup/javascript-style-guide](https://github.com/intercitygroup/javascript-style-guide)
  - **Jam3**: [Jam3/Javascript-Code-Conventions](https://github.com/Jam3/Javascript-Code-Conventions)
  - **JeopardyBot**: [kesne/jeopardy-bot](https://github.com/kesne/jeopardy-bot/blob/master/STYLEGUIDE.md)
  - **JSSolutions**: [JSSolutions/javascript](https://github.com/JSSolutions/javascript)
  - **Kaplan Komputing**: [kaplankomputing/javascript](https://github.com/kaplankomputing/javascript)
  - **KickorStick**: [kickorstick](https://github.com/kickorstick/)
  - **Kinetica Solutions**: [kinetica/javascript](https://github.com/kinetica/Javascript-style-guide)
  - **LEINWAND**: [LEINWAND/javascript](https://github.com/LEINWAND/javascript)
  - **Lonely Planet**: [lonelyplanet/javascript](https://github.com/lonelyplanet/javascript)
  - **M2GEN**: [M2GEN/javascript](https://github.com/M2GEN/javascript)
  - **Mighty Spring**: [mightyspring/javascript](https://github.com/mightyspring/javascript)
  - **MinnPost**: [MinnPost/javascript](https://github.com/MinnPost/javascript)
  - **MitocGroup**: [MitocGroup/javascript](https://github.com/MitocGroup/javascript)
  - **ModCloth**: [modcloth/javascript](https://github.com/modcloth/javascript)
  - **Money Advice Service**: [moneyadviceservice/javascript](https://github.com/moneyadviceservice/javascript)
  - **Muber**: [muber](https://github.com/muber/)
  - **National Geographic**: [natgeo](https://github.com/natgeo/)
  - **Nimbl3**: [nimbl3/javascript](https://github.com/nimbl3/javascript)
  - **NullDev**: [NullDevCo/JavaScript-Styleguide](https://github.com/NullDevCo/JavaScript-Styleguide)
  - **Nulogy**: [nulogy/javascript](https://github.com/nulogy/javascript)
  - **Orange Hill Development**: [orangehill/javascript](https://github.com/orangehill/javascript)
  - **Orion Health**: [orionhealth/javascript](https://github.com/orionhealth/javascript)
  - **OutBoxSoft**: [OutBoxSoft/javascript](https://github.com/OutBoxSoft/javascript)
  - **Peerby**: [Peerby/javascript](https://github.com/Peerby/javascript)
  - **Pier 1**: [Pier1/javascript](https://github.com/pier1/javascript)
  - **Qotto**: [Qotto/javascript-style-guide](https://github.com/Qotto/javascript-style-guide)
  - **Razorfish**: [razorfish/javascript-style-guide](https://github.com/razorfish/javascript-style-guide)
  - **reddit**: [reddit/styleguide/javascript](https://github.com/reddit/styleguide/tree/master/javascript)
  - **React**: [facebook.github.io/react/contributing/how-to-contribute.html#style-guide](https://facebook.github.io/react/contributing/how-to-contribute.html#style-guide)
  - **REI**: [reidev/js-style-guide](https://github.com/rei/code-style-guides/)
  - **Ripple**: [ripple/javascript-style-guide](https://github.com/ripple/javascript-style-guide)
  - **Sainsbury’s Supermarkets**: [jsainsburyplc](https://github.com/jsainsburyplc)
  - **SeekingAlpha**: [seekingalpha/javascript-style-guide](https://github.com/seekingalpha/javascript-style-guide)
  - **Shutterfly**: [shutterfly/javascript](https://github.com/shutterfly/javascript)
  - **Sourcetoad**: [sourcetoad/javascript](https://github.com/sourcetoad/javascript)
  - **Springload**: [springload](https://github.com/springload/)
  - **StratoDem Analytics**: [stratodem/javascript](https://github.com/stratodem/javascript)
  - **SteelKiwi Development**: [steelkiwi/javascript](https://github.com/steelkiwi/javascript)
  - **StudentSphere**: [studentsphere/javascript](https://github.com/studentsphere/guide-javascript)
  - **SwoopApp**: [swoopapp/javascript](https://github.com/swoopapp/javascript)
  - **SysGarage**: [sysgarage/javascript-style-guide](https://github.com/sysgarage/javascript-style-guide)
  - **Syzygy Warsaw**: [syzygypl/javascript](https://github.com/syzygypl/javascript)
  - **Target**: [target/javascript](https://github.com/target/javascript)
  - **Terra**: [terra](https://github.com/cerner?utf8=%E2%9C%93&q=terra&type=&language=)
  - **TheLadders**: [TheLadders/javascript](https://github.com/TheLadders/javascript)
  - **The Nerdery**: [thenerdery/javascript-standards](https://github.com/thenerdery/javascript-standards)
  - **T4R Technology**: [T4R-Technology/javascript](https://github.com/T4R-Technology/javascript)
  - **UrbanSim**: [urbansim](https://github.com/urbansim/)
  - **VoxFeed**: [VoxFeed/javascript-style-guide](https://github.com/VoxFeed/javascript-style-guide)
  - **WeBox Studio**: [weboxstudio/javascript](https://github.com/weboxstudio/javascript)
  - **Weggo**: [Weggo/javascript](https://github.com/Weggo/javascript)
  - **Zillow**: [zillow/javascript](https://github.com/zillow/javascript)
  - **ZocDoc**: [ZocDoc/javascript](https://github.com/ZocDoc/javascript)

**[⬆ về đầu trang](#table-of-contents)**

## <a name="terminology">Danh mục các Thuật ngữ</a>

  Dưới đây là danh mục các từ tiếng Anh tương ứng của các thuật ngữ, và/hoặc các từ, cụm từ mà thông thường không được dịch, như: "style guide", "object", "polyfill", v.v. Các từ, cụm từ được dịch có thể chỉ đúng trong ngữ cảnh là bản dịch này.

  > Nếu bạn cảm thấy một thuật ngữ có vẻ được dịch chưa hợp lý, hoặc bạn cần sự giải thích về một thuật ngữ, bạn có thể mở một [Vấn đề](https://github.com/dangkyokhoang/javascript-style-guide/issues) để thảo luận.
  >
  > Nếu bạn biết một từ/cụm từ tiếng Việt thích hợp hơn cho một thuật ngữ, và nếu bạn sẵn lòng, bạn có thể mở một [Đề nghị kéo](https://github.com/dangkyokhoang/javascript-style-guide/pulls) cho một sửa đổi.

  | Tiếng Việt | English |
  | --- | --- |
  | Ánh xạ | Map/mapping |
  | Ba ngôi | Ternary |
  | Bản sao/sao | Copy |
  | Bản sao nhanh/sao nhanh | Shallow-copy |
  | Bắt | Catch |
  | Bất biến | Immutable |
  | Bẻ nhánh | Fork |
  | Biến | Variable/var |
  | Biến đổi/sự biến đổi | Mutate/mutation |
  | Biểu thức | Expression |
  | Biểu thức hàm | Function expression |
  | Biểu thức hàm gọi tức thời | Immediately invoked function expression/IIFE |
  | Bộ phận hàm | Function signature |
  | Bộ tải | Loader |
  | Bộ tổng hợp | Bundler |
  | Bộ trợ năng | Shim/polyfill |
  | Bước | Step |
  | Cải tiến mã nguồn | Refactor code/code refactoring |
  | Căn đầu dòng | Indent |
  | Câu lệnh/lệnh | Statement |
  | Cấu trúc một dòng | One-liner |
  | Chỉ-viết | Write-only |
  | Chuỗi | String |
  | Chú thích | Comment |
  | Còn-lại | Rest |
  | Cơ số | Radix |
  | Cú pháp | Syntax |
  | Cú pháp tiện lợi | Syntactic sugar |
  | Cũ | Legacy |
  | Dấu gạch dưới | Underscore |
  | Dấu lược/dấu nháy đơn | Single quote |
  | Dấu ngắt dòng/dấu xuống dòng | Line break |
  | Dấu ngoặc | Brace |
  | Dấu ngoặc nhọn | Curly brace |
  | Dấu ngoặc tròn | Parenthesis/parentheses |
  | Dấu ngoặc vuông | Array bracket |
  | Dịch mã | Transpile |
  | Duyệt | Iterate |
  | Đề xuất | Proposal |
  | Đề nghị kéo | Pull request |
  | Định danh | Identifier |
  | Định hướng lối viết |  Style guide |
  | Định nghĩa | Define |
  | Đối số | Argument |
  | Đối tượng | Object |
  | Đối tượng duyệt | Iterator/iterator object |
  | Đối tượng độc nhất | Singleton |
  | Đối tượng khả duyệt | Iterable object |
  | Đối tượng rỗng | Null object |
  | Đối tượng trần | Bare object |
  | Độ bao phủ | Coverage |
  | Đường dẫn | Path |
  | Ép kiểu/sự ép kiểu | Coerce/coercion/cast/casting |
  | Gán/phép gán | Assign/assignment |
  | Gán lại | Reassign |
  | Ghép | Concatenate/concatenation/concat |
  | Giai đoạn chết | Temporal dead zone/TDZ |
  | Giá trị băm | Hash/hash value |
  | Giá trị gốc | Raw value |
  | Giả lập đối tượng | Mock |
  | Giả lập mô-đun | Stub |
  | Giống-mảng | Array-like |
  | Gọi/phép gọi | Call/invoke/invocation |
  | Hàm | Function |
  | Hàm bất định | Variadic function |
  | Hàm bậc cao hơn | Higher-order function |
  | Hàm đọc | Getter/getter function |
  | Hàm ghi | Setter/setter function |
  | Hàm gọi ngược | Callback/callback function |
  | Hàm gọi tức thời | Immediately invoked function |
  | Hàm hữu danh | Named function |
  | Hàm mũi tên | Arrow function |
  | Hàm sinh trị | Generator/generator function |
  | Hàm tạo | Constructor |
  | Hàm thuần | Pure function |
  | Hàm tiện ích | Utility/utility function |
  | Hàm truy cập | Accessor/accessor function |
  | Hàm vô danh | Anonymous function |
  | Hàm xử lý | Handler |
  | Hằng | Constant/const |
  | Hiệu suất | Performance/perf |
  | Hiệu ứng phụ | Side effect |
  | Kéo lên/sự kéo lên/nổi lên/sự nổi lên | Hoist/hoisting |
  | Kê | Pad |
  | Khai báo | Declare/declaration |
  | Khoảng trắng | Whitespace |
  | Không gian tên | Namespace |
  | Khối | Block |
  | Kiểm thử/sự kiểm thử | Test/testing |
  | Kiểu giá trị | Type |
  | Kiểu nguyên thủy | Primitive |
  | Kiểu sai | Falsy/falsey |
  | Ký pháp | Notation |
  | Ký pháp chấm | Dot notation |
  | Ký tự đại diện | Wildcard/wildcard character |
  | Ký tự thoát | Escape character |
  | Liên kết | Link |
  | Liệt kê | Spread |
  | Lô-gíc | Logic |
  | Lỗ hổng | Vulnerability |
  | Lỗi câm | Silent error |
  | Lớp | Class |
  | Lớp cha | Parent class/parent |
  | Lũy thừa | Exponentiation |
  | Lưu tạm | Cache |
  | Lựa chọn | Select/selection |
  | Mã/mã nguồn | Code/source code |
  | Mảng | Array |
  | Mô-đun | Module |
  | Một ngôi | Unary |
  | Ném ra | Throw |
  | Ngăn xếp | Call stack/stack |
  | Ngầm định | Implicit |
  | Nghẽn cổ chai | Bottleneck |
  | Ngoại lệ | Exception |
  | Nguyên mẫu | Prototype |
  | Nguyên văn | Literal |
  | Ngữ cảnh | Context |
  | Nhà phát triển | Developer/dev |
  | Nhập/lệnh nhập | Import |
  | Nối chuỗi | Chain/chaining |
  | Phần tử | Element |
  | Phép dịch chuyển bit | Bit-shift/bit-shift operation |
  | Phép tăng | Increment |
  | Phép giảm | Decrement |
  | Phép tiền tăng/sự tiền tăng | Pre-increment |
  | Phép tiền giảm/sự tiền giảm | Pre-decrement |
  | Phi chuẩn | Non-standard |
  | Phương thức | Method |
  | Quy tắc chèn dấu chấm phẩy tự động | Automatic semicolon insertion/ASI |
  | Quy ước đặt tên | Naming convention |
  | Ràng buộc | Binding |
  | Riêng tư | Private |
  | Rút gọn/dạng rút gọn | Shorthand/shortcut |
  | So sánh/sự so sánh | Compare/comparision |
  | Sự bằng nhau | Equality |
  | Sự kiện | Event/ev |
  | Tên của thuộc tính | Property name/key |
  | Tên được tính của thuộc tính | Computed property name |
  | Tham chiếu | Reference |
  | Tham số | Parameter |
  | Thành viên | Member |
  | Thân hàm | Function body |
  | Thẻ | Tab |
  | Thuộc phạm vi hàm | Function-scoped |
  | Thuộc phạm vi khối | Block-scoped |
  | Thuộc tính | Property |
  | Thư viện | Library/lib |
  | Thừa kế | Inherit/inheritance |
  | Thực thể | Instance |
  | Tiến trình gọi | Caller |
  | Tính khả đọc | Readability |
  | Tính tương thích | Compatibility |
  | Toàn cục | Global |
  | Toán tử | Operator |
  | Trình gỡ lỗi | Debugger |
  | Trình phân tích mã | Linter |
  | Trình thực thi | Engine |
  | Trích xuất/sự trích xuất | Destructure/destructuring/extract |
  | Trọng tải | Payload |
  | Truy cập | Access |
  | Truy vấn | Query |
  | Từ khóa | Keyword |
  | Từ khóa điều chỉnh | Modifier |
  | Ứng dụng | Application/app |
  | Vấn đề | Issue |
  | Xếp tầng | Cascade/cascading |
  | Xuất/lệnh xuất | Export |
  | Xuất hữu danh | Named export |
  | Xuất mặc định | Default export |
  | Xung đột khi gộp | Merge conflict |

**[⬆ về đầu trang](#table-of-contents)**

## <a name="translation">Dịch</a>

  Định hướng này cũng được dịch sang các ngôn ngữ khác:

  - ![en](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/United-States.png) **English (United States)**: [airbnb/javascript](https://github.com/airbnb/javascript)
  - ![br](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Brazil.png) **Brazilian Portuguese**: [armoucar/javascript-style-guide](https://github.com/armoucar/javascript-style-guide)
  - ![bg](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Bulgaria.png) **Bulgarian**: [borislavvv/javascript](https://github.com/borislavvv/javascript)
  - ![ca](https://raw.githubusercontent.com/fpmweb/javascript-style-guide/master/img/catala.png) **Catalan**: [fpmweb/javascript-style-guide](https://github.com/fpmweb/javascript-style-guide)
  - ![cn](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/China.png) **Chinese (Simplified)**: [lin-123/javascript](https://github.com/lin-123/javascript)
  - ![tw](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Taiwan.png) **Chinese (Traditional)**: [jigsawye/javascript](https://github.com/jigsawye/javascript)
  - ![fr](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/France.png) **French**: [nmussy/javascript-style-guide](https://github.com/nmussy/javascript-style-guide)
  - ![de](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Germany.png) **German**: [timofurrer/javascript-style-guide](https://github.com/timofurrer/javascript-style-guide)
  - ![it](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Italy.png) **Italian**: [sinkswim/javascript-style-guide](https://github.com/sinkswim/javascript-style-guide)
  - ![jp](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Japan.png) **Japanese**: [mitsuruog/javascript-style-guide](https://github.com/mitsuruog/javascript-style-guide)
  - ![kr](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/South-Korea.png) **Korean**: [ParkSB/javascript-style-guide](https://github.com/ParkSB/javascript-style-guide)
  - ![ru](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Russia.png) **Russian**: [leonidlebedev/javascript-airbnb](https://github.com/leonidlebedev/javascript-airbnb)
  - ![es](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Spain.png) **Spanish**: [paolocarrasco/javascript-style-guide](https://github.com/paolocarrasco/javascript-style-guide)
  - ![th](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Thailand.png) **Thai**: [lvarayut/javascript-style-guide](https://github.com/lvarayut/javascript-style-guide)
  - ![tr](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Turkey.png) **Turkish**: [eraycetinay/javascript](https://github.com/eraycetinay/javascript)
  - ![ua](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Ukraine.png) **Ukrainian**: [ivanzusko/javascript](https://github.com/ivanzusko/javascript)

## <a name="the-javascript-style-guide-guide">Định hướng Lối viết JavaScript</a>

  - [Lời dẫn](https://github.com/airbnb/javascript/wiki/The-JavaScript-Style-Guide-Guide)

## <a name="chat-with-us-about-javascript">Nói chuyện với Chúng tôi về JavaScript</a>

  - Tìm chúng tôi trên [gitter](https://gitter.im/airbnb/javascript).

## <a name="contributors">Những Người đóng góp</a>

  - [Xem những Người đóng góp](https://github.com/airbnb/javascript/graphs/contributors)

## <a name="license">Giấy phép</a>

(The MIT License)

Copyright (c) 2012 Airbnb

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

**[⬆ về đầu trang](#table-of-contents)**

## <a name="amendments">Các Sửa đổi</a>

Chúng tôi khuyến khích bạn bẻ nhánh bản định hướng này và thay đổi các quy tắc để phù hợp với định hướng lối viết của nhóm của bạn. Dưới đây, bạn có thể liệt kê các sửa đổi đối với bản định hướng này. Điều này cho phép bạn thỉnh thoảng cập nhật lối viết mà không cần giải quyết các xung đột khi gộp.

# };
