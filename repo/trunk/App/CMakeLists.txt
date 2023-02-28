
add_library(
    App
    # Sources #
    ${CMAKE_CURRENT_SOURCE_DIR}/compX/compX.c
    ${CMAKE_CURRENT_SOURCE_DIR}/compY/compY.c
    ${CMAKE_CURRENT_SOURCE_DIR}/compZ/compZ.c
)


target_include_directories(
    App
    PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/compX/
    ${CMAKE_CURRENT_SOURCE_DIR}/compY/
    ${CMAKE_CURRENT_SOURCE_DIR}/compZ/
)

target_link_libraries(
    App 
    # Dependencies #
    PRIVATE
)