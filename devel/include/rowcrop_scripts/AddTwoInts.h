// Generated by gencpp from file rowcrop_scripts/AddTwoInts.msg
// DO NOT EDIT!


#ifndef ROWCROP_SCRIPTS_MESSAGE_ADDTWOINTS_H
#define ROWCROP_SCRIPTS_MESSAGE_ADDTWOINTS_H

#include <ros/service_traits.h>


#include <rowcrop_scripts/AddTwoIntsRequest.h>
#include <rowcrop_scripts/AddTwoIntsResponse.h>


namespace rowcrop_scripts
{

struct AddTwoInts
{

typedef AddTwoIntsRequest Request;
typedef AddTwoIntsResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct AddTwoInts
} // namespace rowcrop_scripts


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::rowcrop_scripts::AddTwoInts > {
  static const char* value()
  {
    return "6a2e34150c00229791cc89ff309fff21";
  }

  static const char* value(const ::rowcrop_scripts::AddTwoInts&) { return value(); }
};

template<>
struct DataType< ::rowcrop_scripts::AddTwoInts > {
  static const char* value()
  {
    return "rowcrop_scripts/AddTwoInts";
  }

  static const char* value(const ::rowcrop_scripts::AddTwoInts&) { return value(); }
};


// service_traits::MD5Sum< ::rowcrop_scripts::AddTwoIntsRequest> should match
// service_traits::MD5Sum< ::rowcrop_scripts::AddTwoInts >
template<>
struct MD5Sum< ::rowcrop_scripts::AddTwoIntsRequest>
{
  static const char* value()
  {
    return MD5Sum< ::rowcrop_scripts::AddTwoInts >::value();
  }
  static const char* value(const ::rowcrop_scripts::AddTwoIntsRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::rowcrop_scripts::AddTwoIntsRequest> should match
// service_traits::DataType< ::rowcrop_scripts::AddTwoInts >
template<>
struct DataType< ::rowcrop_scripts::AddTwoIntsRequest>
{
  static const char* value()
  {
    return DataType< ::rowcrop_scripts::AddTwoInts >::value();
  }
  static const char* value(const ::rowcrop_scripts::AddTwoIntsRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::rowcrop_scripts::AddTwoIntsResponse> should match
// service_traits::MD5Sum< ::rowcrop_scripts::AddTwoInts >
template<>
struct MD5Sum< ::rowcrop_scripts::AddTwoIntsResponse>
{
  static const char* value()
  {
    return MD5Sum< ::rowcrop_scripts::AddTwoInts >::value();
  }
  static const char* value(const ::rowcrop_scripts::AddTwoIntsResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::rowcrop_scripts::AddTwoIntsResponse> should match
// service_traits::DataType< ::rowcrop_scripts::AddTwoInts >
template<>
struct DataType< ::rowcrop_scripts::AddTwoIntsResponse>
{
  static const char* value()
  {
    return DataType< ::rowcrop_scripts::AddTwoInts >::value();
  }
  static const char* value(const ::rowcrop_scripts::AddTwoIntsResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ROWCROP_SCRIPTS_MESSAGE_ADDTWOINTS_H
