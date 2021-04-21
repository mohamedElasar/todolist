import 'dart:convert';
import 'package:example/models/http_exception.dart';
import 'package:flutter/widgets.dart';
import 'package:http/http.dart' as http;

class Auth with ChangeNotifier {
  String _token;
  DateTime _expiryDate;
  String _userId;
  String _email;
  String _name;

  bool get isAuth {
    return token != null;
  }

  String get token {
    if (_token != null) {
      return _token;
    }
    return null;
  }

  String get email {
    return _email;
  }

  String get name {
    return _name;
  }

  String get userId {
    return _userId;
  }

  Future<void> register(
      String username, String email, String password1, String password2) async {
    final url = 'http://10.0.2.2:8000/api/rest-auth/registration/';
    try {
      final response = await http.post(
        url,
        body: json.encode(
          {
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2,
          },
        ),
        headers: {'Content-Type': 'application/json'},
      );
      final data = json.decode(response.body);
      final list_data = data.values.toList();
      final keys_data = data.keys.toList();
      print(list_data[0][0]);
      if (!keys_data.contains('key') || response.statusCode == 400) {
        throw HttpException(list_data[0][0]);
      } else {
        _token = list_data[0];
        print(_token);
      }
      notifyListeners();
    } catch (error) {
      throw HttpException(error.toString());
    }
  }

  Future<void> login(String email, String password) async {
    final url = 'http://10.0.2.2:8000/api/todos/rest-auth/login/';
    try {
      final response = await http.post(
        url,
        body: json.encode(
          {
            'username': email,
            'email': email,
            'password': password,
          },
        ),
        headers: {'Content-Type': 'application/json'},
      );
      final data = json.decode(response.body);
      final list_data = data.values.toList();
      final keys_data = data.keys.toList();
      print(list_data[0][0]);
      if (!keys_data.contains('key') || response.statusCode == 400) {
        throw HttpException(list_data[0][0]);
      } else {
        _token = list_data[0];
        print(_token);
      }
      notifyListeners();
    } catch (error) {
      throw HttpException(error.toString());
    }
  }
}
